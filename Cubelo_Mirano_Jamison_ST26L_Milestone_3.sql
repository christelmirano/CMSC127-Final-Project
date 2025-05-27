-- MILESTONE 3

-- CREATE OR REPLACE USER 'root'@'localhost' IDENTIFIED BY 'mysqlpw';
-- GRANT ALL PRIVILEGES ON org_membership

-- Dumping database structure for org_membership
DROP DATABASE IF EXISTS `org_membership`;

-- Create the database
CREATE DATABASE IF NOT EXISTS `org_membership`;
USE `org_membership`;

GRANT ALL ON org_membership.* TO 'project127'@'localhost';

-- Create MEMBER Table
DROP TABLE IF EXISTS `member`;
CREATE TABLE IF NOT EXISTS `member` (
    student_id VARCHAR(11) PRIMARY KEY,
    degree_program VARCHAR(50) NOT NULL,
    role ENUM('President', 'Vice President', 'Secretary', 'Member'),
    batch INT NOT NULL,
    status ENUM('Active', 'Inactive', 'Expelled', 'Suspended', 'Alumni'),
    committee VARCHAR(50),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10)
);

-- create ORGANIZATION Table
DROP TABLE IF EXISTS `organization`;
CREATE TABLE IF NOT EXISTS `organization` (
    organization_id VARCHAR(11) PRIMARY KEY,
    organization_name VARCHAR(100) NOT NULL,
    organization_type ENUM('Academic', 'Non-academic', 'Varsitarian')
);

-- create FEE Table
DROP TABLE IF EXISTS `fee`;
CREATE TABLE IF NOT EXISTS `fee` (
    payment_id VARCHAR(11) PRIMARY KEY,
    due_date DATE,
    purpose VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2), -- 2 decimal places
    organization_id VARCHAR(11),
    FOREIGN KEY (organization_id ) REFERENCES organization(organization_id) ON DELETE SET NULL
);

-- create MEMBER_HAS_ORGANIZATION Table
DROP TABLE IF EXISTS `member_has_organization`;
CREATE TABLE IF NOT EXISTS `member_has_organization` (
    student_id VARCHAR(11),
    organization_id VARCHAR(11),
    semester ENUM('First', 'Second', 'Midyear'),
    PRIMARY KEY (student_id, organization_id, semester),
    FOREIGN KEY (student_id) REFERENCES member(student_id),
    FOREIGN KEY (organization_id) REFERENCES organization(organization_id)
);

-- create MEMBER_PAYS_FEE Table
DROP TABLE IF EXISTS `member_pays_fee`;
CREATE TABLE IF NOT EXISTS `member_pays_fee` (
    student_id VARCHAR(11),
    payment_id VARCHAR(11),
    payment_status ENUM('Paid', 'Unpaid'),
    on_time_status ENUM('On time', 'Late'),
    payment_date DATE,
    PRIMARY KEY (student_id, payment_id),
    FOREIGN KEY (student_id) REFERENCES member(student_id),
    FOREIGN KEY (payment_id) REFERENCES fee(payment_id)
);

-- create Member_Has_Organization_And_Fee Table
DROP TABLE IF EXISTS `member_has_organization_and_fee`;
CREATE TABLE IF NOT EXISTS `member_has_organization_and_fee` (
    student_id VARCHAR(11),
    organization_id VARCHAR(11),
    payment_id VARCHAR(11),
    semester ENUM('First', 'Second', 'Midyear'),
    PRIMARY KEY (student_id, organization_id, payment_id, semester),
    FOREIGN KEY (student_id) REFERENCES member(student_id),
    FOREIGN KEY (organization_id) REFERENCES organization(organization_id),
    FOREIGN KEY (payment_id) REFERENCES fee(payment_id)
);

-- MEMBER
INSERT INTO `member` (`student_id`, `degree_program`, `role`, `batch`, `status`, `gender`, `committee`, `first_name`, `last_name`) VALUES
    ('2023-01234', 'BS Computer Science', 'President', 2023, 'Active', 'Male', 'Events', 'Andrew', 'Elizalde'),
    ('2023-01666', 'BS Computer Science', 'Member', 2023, 'Expelled', 'Male', 'Events', 'Hannah', 'Monterde'),
    ('2023-12345', 'BS Computer Science', 'Secretary', 2023, 'Active', 'Female', 'Executive', 'Leon', 'Jamison'),
    ('2022-03456', 'BS Applied Mathematics', 'Vice President', 2022, 'Active', 'Female', 'Finance', 'Ange', 'Smith'),
    ('2023-38465', 'BS Biology', 'Member', 2023, 'Inactive', 'Male', 'Logistics', 'Mark', 'Lee'),
    ('2021-98765', 'BS Chemistry', 'Member', 2021, 'Active', 'Female', 'Media', 'Christel', 'Galvez'),
    ('2022-11112', 'BS Computer Science', 'Member', 2022, 'Active', 'Female', 'Media', 'Alice', 'Tan'),
    ('2021-22223', 'BS Information Systems', 'Member', 2021, 'Alumni', 'Male', 'Finance', 'John', 'Doe'),
    ('2023-33334', 'BS Biology', 'Secretary', 2023, 'Active', 'Female', 'Logistics', 'Jane', 'Lopez'),
    ('2023-44445', 'BS Chemistry', 'Vice President', 2023, 'Active', 'Male', 'Executive', 'Paul', 'Yu'),
    ('2022-55556', 'BS Applied Mathematics', 'President', 2022, 'Suspended', 'Female', 'Membership', 'Sophie', 'Lim'),
    ('2021-66667', 'BS Physics', 'Member', 2021, 'Active', 'Male', 'Events', 'Kyle', 'Reyes'),
    ('2023-77778', 'BS Computer Science', 'Member', 2023, 'Active', 'Female', 'Media', 'Clara', 'Santos'),
    ('2022-88889', 'BS Computer Engineering', 'Member', 2022, 'Inactive', 'Male', 'Finance', 'Miguel', 'Ong'),
    ('2024-99990', 'BS Mathematics', 'Member', 2024, 'Active', 'Female', 'Logistics', 'Luna', 'Ramos'),
    ('2023-00001', 'BS Statistics', 'Member', 2023, 'Active', 'Male', 'Membership', 'Brian', 'Tan'),
    ('2023-20001', 'BS Math', 'Member', 2023, 'Active', 'Female', 'Finance', 'Ivy', 'Chen'),
    ('2023-20002', 'BS Math', 'Member', 2023, 'Active', 'Male', 'Logistics', 'Eli', 'Nguyen'),
    ('2023-20003', 'BS Math', 'Member', 2023, 'Active', 'Female', 'Media', 'Grace', 'Tan'),
    ('2023-20004', 'BS Math', 'Member', 2023, 'Active', 'Male', 'Events', 'Zane', 'Rivera'),
    ('2023-20005', 'BS Math', 'Member', 2023, 'Active', 'Female', 'Executive', 'Mia', 'Lim'),
    ('2023-20006', 'BS Math', 'Member', 2023, 'Active', 'Male', 'Membership', 'Noel', 'Santos'),
    ('2023-20007', 'BS Math', 'Member', 2023, 'Active', 'Female', 'Finance', 'Ella', 'Reyes'),
    ('2023-20008', 'BS Math', 'Member', 2023, 'Active', 'Male', 'Logistics', 'Sean', 'Velasquez'),
    ('2023-20009', 'BS Math', 'Member', 2023, 'Active', 'Female', 'Media', 'Lena', 'Chavez'),
    ('2023-20010', 'BS Math', 'Member', 2023, 'Active', 'Male', 'Events', 'Kai', 'Mendoza');

-- ORGANIZATION
INSERT INTO `organization` (`organization_id`, `organization_name`, `organization_type`) VALUES
    ('ORG001', 'Compsci Cuties', 'Academic'),
    ('ORG002', 'Hello 127 World', 'Academic'),
    ('ORG003', 'CHRONAN', 'Varsitarian'),
    ('ORG004', 'CS ORG ', 'Academic'),
    ('ORG005', 'ilove127', 'Academic'),   
    ('ORG006', 'BioNexus', 'Academic'),
    ('ORG007', 'Stats Society', 'Academic'),
    ('ORG008', 'Math Wizards', 'Academic'),
    ('ORG009', 'Physics People', 'Academic'),
    ('ORG010', 'Chem Champs', 'Academic'),
    ('ORG011', 'ComSci Circle', 'Academic'),
    ('ORG012', 'Media Makers', 'Non-academic'),
    ('ORG013', 'Finance Force', 'Academic'),
    ('ORG014', 'Eco Engage', 'Non-academic'),
    ('ORG015', 'Varsity Voices', 'Varsitarian');

 -- FEE
INSERT INTO `fee` (`payment_id`, `due_date`, `purpose`, `amount`, `organization_id`) VALUES
    ('FEE001', '2025-01-15', 'Membership Fee', 50.00,  'ORG001'),
    ('FEE002', '2025-01-20', 'Membership Fee', 30.00, 'ORG002'),
    ('FEE003', '2025-02-10', 'Event Fee', 20.00, 'ORG003'),
    ('FEE004', '2025-03-01', 'Late payment', 100.00, 'ORG004'),
    ('FEE005', '2025-04-01', 'Event Fee', 75.00, 'ORG005'),
    ('FEE006', '2025-05-01', 'Membership Fee', 60.00, 'ORG006'),
    ('FEE007', '2025-05-15', 'Event Contribution', 25.00, 'ORG007'),
    ('FEE008', '2025-06-01', 'Seminar Fee', 40.00, 'ORG008'),
    ('FEE009', '2025-06-15', 'Membership Fee', 50.00, 'ORG009'),
    ('FEE010', '2025-07-01', 'Fundraiser Support', 20.00, 'ORG010'),
    ('FEE011', '2025-07-15', 'Annual Dues', 35.00, 'ORG011'),
    ('FEE012', '2025-08-01', 'Workshop Fee', 45.00, 'ORG012'),
    ('FEE013', '2025-08-15', 'Membership Fee', 55.00, 'ORG013'),
    ('FEE014', '2025-09-01', 'Event Fee', 70.00, 'ORG014'),
    ('FEE015', '2025-09-15', 'Varsity Contribution', 80.00, 'ORG015'),
    ('FEE016', '2025-04-15', 'Membership Fee', 50.00, 'ORG001'), 
    ('FEE017', '2025-04-16', 'Membership Fee', 50.00, 'ORG002'), 
    ('FEE018', '2025-04-17', 'Membership Fee', 50.00, 'ORG003'), 
    ('FEE019', '2025-04-18', 'Membership Fee', 50.00, 'ORG004');

-- MEMBER_HAS_ORGANIZATION
INSERT INTO `member_has_organization` (`student_id`, `organization_id`, `semester`) VALUES
    ('2023-01234', 'ORG001', 'First'),
    ('2022-03456', 'ORG002', 'Second'),
    ('2023-38465', 'ORG003', 'Midyear'),
    ('2021-98765', 'ORG004', 'Second'),
    ('2023-12345', 'ORG005', 'First'),
    ('2022-11112', 'ORG006', 'Second'),
    ('2021-22223', 'ORG007', 'Midyear'),
    ('2023-33334', 'ORG008', 'First'),
    ('2023-44445', 'ORG009', 'Second'),
    ('2022-55556', 'ORG010', 'First'),
    ('2021-66667', 'ORG011', 'Second'),
    ('2023-77778', 'ORG012', 'Midyear'),
    ('2022-88889', 'ORG013', 'First'),
    ('2024-99990', 'ORG014', 'Second'),
    ('2023-00001', 'ORG015', 'Midyear'),
    ('2023-20001', 'ORG001', 'First'),
    ('2023-20002', 'ORG001', 'First'),
    ('2023-20003', 'ORG001', 'First'),
    ('2023-20004', 'ORG001', 'First'),
    ('2023-20005', 'ORG002', 'Second'),
    ('2023-20006', 'ORG002', 'Second'),
    ('2023-20007', 'ORG002', 'Second'),
    ('2023-20008', 'ORG002', 'Second'),
    ('2023-20001', 'ORG003', 'Midyear'),
    ('2023-20002', 'ORG003', 'Midyear'),
    ('2023-20003', 'ORG003', 'Midyear'),
    ('2023-20004', 'ORG003', 'Midyear'),
    ('2023-20005', 'ORG004', 'First'),
    ('2023-20006', 'ORG004', 'First'),
    ('2023-20007', 'ORG004', 'First'),
    ('2023-20008', 'ORG004', 'First');

-- MEMBER_PAYS_FEE
INSERT INTO `member_pays_fee` (`student_id`, `payment_id`, `payment_status`, `on_time_status`, `payment_date`) VALUES
('2023-01234', 'FEE001', 'Paid', 'On time', '2025-01-10'),
('2022-03456','FEE002', 'Paid', 'On time', '2023-01-10'),
('2023-38465', 'FEE003', 'Paid', 'On time', '2023-01-10'),
('2021-98765', 'FEE004', 'Paid', 'On time', '2023-01-10'),
('2023-12345', 'FEE005', 'Paid', 'On time', '2023-01-10'),
('2022-11112', 'FEE006', 'Paid', 'On time', '2025-04-25'),
('2021-22223', 'FEE007', 'Unpaid', 'Late', NULL),
('2023-33334', 'FEE008', 'Paid', 'Late', '2025-06-05'),
('2023-44445', 'FEE009', 'Paid', 'On time', '2025-06-10'),
('2022-55556', 'FEE010', 'Unpaid', 'Late', NULL),
('2021-66667', 'FEE011', 'Paid', 'On time', '2025-07-10'),
('2023-77778', 'FEE012', 'Paid', 'Late', '2025-08-10'),
('2022-88889', 'FEE013', 'Paid', 'On time', '2025-08-12'),
('2024-99990', 'FEE014', 'Unpaid', 'Late', NULL),
('2023-00001', 'FEE015', 'Paid', 'On time', '2025-09-10'),
('2023-20001', 'FEE006', 'Paid', 'On time', '2025-04-01'),
('2023-20005', 'FEE007', 'Paid', 'On time', '2025-04-01'),
('2023-20002', 'FEE008', 'Paid', 'On time', '2025-04-01'),
('2023-20006', 'FEE009', 'Paid', 'On time', '2025-04-01');

-- MEMBER_HAS_ORGANIZATION_AND_FEE
INSERT INTO `member_has_organization_and_fee` (`student_id`, `organization_id`, `payment_id`, `semester`) VALUES
('2023-01234', 'ORG001', 'FEE001' , 'First'),
('2022-03456', 'ORG002','FEE002', 'Second'),
('2023-38465', 'ORG003', 'FEE003', 'Midyear'),
('2021-98765', 'ORG004', 'FEE004', 'Second'),
('2023-12345', 'ORG005', 'FEE005', 'First'),
('2022-11112', 'ORG006', 'FEE006', 'Second'),
('2021-22223', 'ORG007', 'FEE007', 'Midyear'),
('2023-33334', 'ORG008', 'FEE008', 'First'),
('2023-44445', 'ORG009', 'FEE009', 'Second'),
('2022-55556', 'ORG010', 'FEE010', 'First'),
('2021-66667', 'ORG011', 'FEE011', 'Second'),
('2023-77778', 'ORG012', 'FEE012', 'Midyear'),
('2022-88889', 'ORG013', 'FEE013', 'First'),
('2024-99990', 'ORG014', 'FEE014', 'Second'),
('2023-00001', 'ORG015', 'FEE015', 'Midyear'),
('2023-20001', 'ORG001', 'FEE006', 'First'),
('2023-20005', 'ORG002', 'FEE007', 'Second'),
('2023-20002', 'ORG003', 'FEE008', 'Midyear'),
('2023-20006', 'ORG004', 'FEE009', 'First');

-- SELECT: SELECT ACADEMIC-TYPE ORGS
SELECT * FROM organization WHERE organization_type='Academic';

-- UPDATE : INCREASE MEMBERSHIP FEE BY 30%
UPDATE fee  SET amount = amount * 1.3 WHERE purpose = 'Membership Fee';

-- DELETE: DELETE EXPELLED MEMBERS
DELETE FROM member WHERE status='Expelled';

-- to check which organization has > 1 committees
SELECT mho.organization_id
FROM member_has_organization mho
JOIN member m ON mho.student_id = m.student_id
WHERE m.committee IS NOT NULL
GROUP BY mho.organization_id
HAVING COUNT(DISTINCT m.committee) > 1;

