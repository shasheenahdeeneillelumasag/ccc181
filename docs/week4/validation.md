# Validation

| Rule | Layer | How I tested it | What happened |
| --- | --- | --- | --- |
| Name must not be empty | Flask | `curl.exe` POST to `/join` with `name=` | HTTP/1.1 400 BAD REQUEST |
| Number of family members must be at least 1 (and at most 100) | Flask | `curl.exe` with `household_size=0` | HTTP/1.1 400 BAD REQUEST |
| Barangay must exist | Flask | `curl.exe` with `barangay_id=999` | HTTP/1.1 400 BAD REQUEST |
| Name is at most 100 characters | Flask | `curl.exe` with a name of 150 letters | HTTP/1.1 400 BAD REQUEST |
| A switched-off barangay cannot be chosen | Flask | Switched a barangay off, then `curl.exe` with its `barangay_id` | HTTP/1.1 400 BAD REQUEST |
| A family with an open ticket cannot join again | Flask | Joined twice with the same name | `ERROR: duplicate key value violates unique constraint "uq_tickets_one_open_per_family"` |
| FOREIGN KEY: a family needs a real barangay | Database | `INSERT INTO families (head_name, household_size, barangay_id) VALUES ('Test Family', 3, 999);` in psql | `ERROR: insert or update on table "families" violates foreign key constraint "families_barangay_id_fkey"` |
| FOREIGN KEY: a ticket needs a real family | Database | `INSERT INTO tickets (family_id) VALUES (999);` | `ERROR: insert or update on table "tickets" violates foreign key constraint "tickets_family_id_fkey"` |
| CHECK: status must be one of five values | Database | `UPDATE tickets SET status = 'lost' WHERE id = 1;` | `ERROR: new row for relation "tickets" violates check constraint "ck_tickets_status"` |
| CHECK: household size is at least 1 | Database | `INSERT INTO families (head_name, household_size, barangay_id) VALUES ('Zero Family', 0, 1);` | `ERROR: new row for relation "families" violates check constraint "ck_families_household_size"` |
| CHECK: called_at is not before created_at | Database | `UPDATE tickets SET called_at = created_at - interval '1 hour' WHERE id = 1;` | `ERROR: new row for relation "tickets" violates check constraint "ck_tickets_called_at_after_created"` |
| UNIQUE: a barangay name appears once | Database | `INSERT INTO barangays (name, slot_time) VALUES ('Barangay Tibanga', '08:00');` | `ERROR: duplicate key value violates unique constraint "barangays_name_key"` |
| UNIQUE: a family appears once in a barangay | Database | `INSERT INTO families` with a name and barangay that already exist | `ERROR: duplicate key value violates unique constraint "uq_families_barangay_head_name"` |
| UNIQUE (partial): one open ticket per family | Database | `INSERT INTO tickets (family_id) VALUES (10);` | `ERROR: duplicate key value violates unique constraint "uq_tickets_one_open_per_family"` |
| NOT NULL: a barangay needs a time slot | Database | `INSERT INTO barangays (name) VALUES ('No Time Barangay');` | `ERROR: null value in column "slot_time" of relation "barangays" violates not-null constraint` |
| RESTRICT: a barangay with families cannot be deleted | Database | `DELETE FROM barangays WHERE id = 1;` | `ERROR: update or delete on table "barangays" violates foreign key constraint "families_barangay_id_fkey" on table "families"` |