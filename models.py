from datetime import datetime, time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, String, Time, UniqueConstraint, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Barangay(db.Model):
    __tablename__ = "barangays"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True)
    slot_time: Mapped[time] = mapped_column(Time, nullable=False)

    families: Mapped[list["Family"]] = relationship(back_populates="barangay")

class Family(db.Model):
    __tablename__ = "families"

    id: Mapped[int] = mapped_column(primary_key=True)
    head_name: Mapped[str] = mapped_column(String(100))
    household_size: Mapped[int] = mapped_column()
    barangay_id: Mapped[int] = mapped_column(
        ForeignKey("barangays.id", ondelete="RESTRICT")
    )
    barangay: Mapped["Barangay"] = relationship(back_populates="families")
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="family")

    __table_args__ = (
        CheckConstraint("length(trim(head_name)) > 0", name="ck_families_head_name"),
        CheckConstraint("household_size >= 1", name="ck_families_household_size"),
        UniqueConstraint("barangay_id", "head_name", name="uq_families_barangay_head_name"),
    )

class Ticket(db.Model):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    family_id: Mapped[int] = mapped_column(
        ForeignKey("families.id", ondelete="RESTRICT"), index=True
    )
    status: Mapped[str] = mapped_column(
        String(20), default="waiting", server_default="waiting"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    called_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    family: Mapped["Family"] = relationship(back_populates="tickets")

    __table_args__ = (
        CheckConstraint(
            "status IN ('waiting', 'called', 'received', 'no-show', 'left')",
            name="ck_tickets_status",
        ),
        CheckConstraint(
            "called_at IS NULL OR called_at >= created_at",
            name="ck_tickets_called_at_after_created",
        ),
        Index(
            "uq_tickets_one_open_per_family",
            "family_id",
            unique=True,
            postgresql_where=text("status IN ('waiting', 'called')"),
        ),
        Index(
            "uq_tickets_one_received_per_family",
            "family_id",
            unique=True,
            postgresql_where=text("status = 'received'"),
        ),
    )