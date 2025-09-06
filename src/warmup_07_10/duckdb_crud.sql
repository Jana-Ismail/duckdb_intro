CREATE SEQUENCE IF NOT EXISTS warmups_id_seq START 1;

CREATE TABLE warmups (
    warmup_id INTEGER DEFAULT nextval('warmups_id_seq') PRIMARY KEY,
    team_id INT NOT NULL,
    warmup_date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    duration INT CHECK (duration >= 0),
);

SELECT * FROM warmups;

INSERT INTO warmups (team_id, warmup_date, location, duration) VALUES
-- do nto include warmup_id since it is auto-incremented                                                                   (
(1, '2023-10-01', 'Station A', 60),
(2, '2023-10-02', 'Stadium B', 45),
(1, '2023-10-03', 'Stadium C', 30),
(3, '2023-10-04', 'Stadium D', 90);

--wrap updates in a transaction (usually)
BEGIN TRANSACTION;
SELECT * FROM warmups;
UPDATE warmups SET
    location = 'Stadium E',
    duration = 50
WHERE warmup_id = 1;
SELECT * FROM warmups;
--     ROLLBACK;
COMMIT
SELECT * FROM warmups;

BEGIN TRANSACTION;
SELECT * FROM warmups;
DELETE FROM warmups WHERE warmup_id = 2;
SELECT * FROM warmups;
-- ROLLBACK;
COMMIT;
SELECT * FROM warmups;
