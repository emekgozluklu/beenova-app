/*ADMIN*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('admin', 'admin', 'admin', 'admin@admin.com', 1, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 1, 1, 1, '2023-01-01 00:00:00', null, 'instance/uploads/1/pp1.jpg');

/*EMPLOYEES*/
/*Company admins*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Joe', 'Perier', 'JoePerier', 'joe@peri.com', 2, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 1, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/2/pp2.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Angela', 'Putzmeisterer', 'AngelaPutzmeisterer', 'angela@putzmeister.com', 3, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 1, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/3/pp3.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Donald', 'Holcimer', 'DonaldHolcimer', 'donald@holcim.com', 4, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 1, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/4/pp4.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Emanuel', 'Bögler', 'Emanuel Bögler', 'emanuel@maxbogl.com', 5, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 1, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/5/pp5.jpg');



/*PERI users*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('John', 'Perier', 'JohnPerier', 'john@peri.com', 2, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/2/pp3.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Lombard', 'Perier', 'LombardPerier', 'lombard@peri.com', 2, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/2/pp4.jpg');


/*Putzmeister users*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Michael', 'Putzmeisterer', 'MichaelPutzmeisterer', 'michael@putzmeister.com', 3, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/3/pp3.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Ignacio', 'Putzmeisterer', 'IgnacioPutzmeisterer', 'ignacio@putzmeister.com', 3, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/3/pp3.jpg');


/*HOLCIM users*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Marlo', 'Holcimer', 'MarloHolcimer', 'marlo@holcim.com', 4, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/4/pp4.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Bryan', 'Holcimer', 'BryanHolcimer', 'bryan@holcim.com', 4, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/4/pp4.jpg');


/*Max Bögl users*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Marlo', 'Bögler', 'Marlo Bögler', 'marlo@maxbogl.com', 5, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/5/pp5.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('Christi', 'Bögler', 'Christi Bögler', 'christi@maxbogl.com', 5, '+491111111111', 'pbkdf2:sha256:260000$7LK48Ms896Po9e5G$bc6e85d825eca89d90750a83cff5109de7fe5cfe360810f9e6679f1ed6706ce5', 0, 0, 1, '2023-01-01 00:00:00', 1, 'instance/uploads/5/pp5.jpg');


/*COMPANIES*/
INSERT INTO company (name, registered_at, admin_id)
VALUES ('Beenova', '2023-01-01 00:00:00', 1);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('PERI', '2023-01-01 00:00:00', 2);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('Putzmeister', '2023-01-01 00:00:00', 3);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('HOLCIM', '2023-01-01 00:00:00', 4);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('Max Bögl', '2023-01-01 00:00:00', 5);



/*data source type*/
INSERT INTO data_source_type (name, description)
VALUES ('CSV', 'CSV File');

INSERT INTO data_source_type (name, description)
VALUES ('JSON', 'JSON File');

INSERT INTO data_source_type (name, description)
VALUES ('SQL', 'SQL Database Table');

INSERT INTO data_source_type (name, description)
VALUES ('Sensor (Real Time)', 'Real Time data from sensors');



/*DATA SOURCES*/
/*Beenova*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Cement Manufacturing', '', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 1, '', 0, 0, 1, 1, '', '');


/*HOLCIM*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('CO2 Emissions of Products', '', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 1, '', 0, 0, 4, 4, '', '');

insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Silo stocks', 'Up to date silo stocks.', '2023-01-15 09:14:13', '2023-01-18 09:14:13', 1, 1, '', 0, 0, 4, 4, '', '');


/*PERI*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Projects (Active and Historical)', '', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 3, '', 0, 0, 2, 2, '', '');

insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Concrete Humidity by Time', 'Real time data from sensors in the construction site. Data includes timestamp and the humidity of the concrete.', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 4, '', 0, 0, 2, 2, '', '');


/*Max Bögl*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Construction Site Sensor Data', 'Collection of datas point collected from construction site. Filter by project_id and sensor_id to get the result of a specific sensor by time.', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 1, '', 0, 0, 5, 5, '', '');


/*Putzmeister*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by, database_table_name, url_endpoint)
values ('Concrete Humidity in Mixer', '', '2023-01-18 09:14:13', '2023-01-18 09:14:13', 1, 1, '', 0, 0, 3, 3, '', '');


INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (1, 2, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (1, 3, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (1, 4, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (2, 2, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (2, 2, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (3, 2, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);

INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
VALUES (4, 2, '2023-01-01 00:00:00', '2023-01-05 00:00:00', 735142, null);