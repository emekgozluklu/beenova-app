/*admin user*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('admin', 'admin', 'admin', 'admin@admin.com', 1, '1251234', 'pbkdf2:sha256:260000$n2ojqTTcttDFIR2G$d4ce12d96b2684eef4645223c2fb3897e5a094fdee4f0e7c662c380cd4b255d1', 1, 1, 1, '2019-01-01 00:00:00', 1, 'instance/uploads/1/profile_photo.jpg');

/*employee users*/
INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('user', 'user', 'user', 'user@user.com', 1, '1251234', 'pbkdf2:sha256:260000$L7XVoYy8VtMZWtoU$43a595efacc21d58bf5129f154b9ce5cfa8edc5defb9d32bc8fb2ac09fab3412', 0, 1, 1, '2019-01-01 00:00:00', 1, 'instance/uploads/1/profile_photo2.jpg');

INSERT INTO employee (first_name, last_name, username, email, company, phone_number, password_hash, is_admin, is_company_admin, is_activated, created_at, created_by, profile_photo)
VALUES ('user2', 'user2', 'user2', 'user2@user2.com', 2, '1251234', 'pbkdf2:sha256:260000$4RjAkXY1sci95QQr$2c5ce371d17c175b7b47bf0e6b772de534de424dc54b9eca5fb6af11c0ffb60c', 0, 1, 1, '2019-01-01 00:00:00', 1, 'instance/uploads/1/profile_photo3.jpg');

/*company*/
INSERT INTO company (name, registered_at, admin_id)
VALUES ('beenova', '2019-01-01 00:00:00', 1);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('holcim', '2019-01-01 00:00:00', 2);

INSERT INTO company (name, registered_at, admin_id)
VALUES ('peri', '2019-01-01 00:00:00', 3);

/*data source type*/
INSERT INTO data_source_type (name, description)
VALUES ('csv', 'CSV File');

INSERT INTO data_source_type (name, description)
VALUES ('json', 'JSON File');

INSERT INTO data_source_type (name, description)
VALUES ('xml', 'XML File');

INSERT INTO data_source_type (name, description)
VALUES ('sql', 'SQL Database');

/*data source*/
insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Concrete Formula', 'Concrete Formula', '2023-01-01 00:00:00', '2023-01-01 00:00:00', 1, 1, 'instance/uploads/1/data_source_1.csv', 0, 0, 1, 1);

insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Pump Data/Moisture', 'Moisture content information coming from pumps.', '2022-11-22 00:00:00', '2022-11-22 00:00:00', 1, 2, 'instance/uploads/1/data_source_2.csv', 0, 0, 1, 1);

insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Concrete Intensity Experiment History', 'Experiment history of 20 years.', '2019-01-01 00:00:00', '2019-01-01 00:00:00', 1, 3, 'instance/uploads/1/data_source_3.csv', 0, 0, 1, 1);

insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Mock Data 1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque, lectus a luctus sagittis, magna eros auctor augue, vitae maximus dui arcu ac leo. Ut fermentum sagittis eros vulputate porta. Cras pulvinar eget augue ac dignissim. Vivamus id posuere augue, vel mattis eros. Curabitur ac odio vitae ante congue vestibulum. Morbi consectetur in lacus sit amet consequat. Aenean tristique lacinia dapibus. Nam viverra risus diam, vitae dapibus turpis hendrerit sit amet.', '2019-01-01 00:00:00', '2019-01-01 00:00:00', 1, 3, 'instance/uploads/1/data_source_3.csv', 0, 0, 1, 1);


insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Mock Data 2', 'Suspendisse at magna in lectus rhoncus posuere ac sed nunc. Integer tincidunt ipsum quis commodo gravida. Vestibulum pharetra nisl elementum mauris rutrum, nec vestibulum nisl elementum. In lobortis quam at porta suscipit. Duis interdum at libero non rhoncus. Suspendisse potenti. Nunc pellentesque accumsan aliquam. Quisque magna lorem, faucibus ac interdum et, porttitor ac lectus.', '2019-01-01 00:00:00', '2019-01-01 00:00:00', 1, 1, 'instance/uploads/1/data_source_3.csv', 0, 0, 1, 1);


insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Mock Data 3', 'In hac habitasse platea dictumst. Curabitur enim enim, tempus a rutrum sed, venenatis et eros. Integer magna mi, molestie et risus quis, gravida ullamcorper ex. Ut accumsan condimentum venenatis. Vestibulum congue feugiat ante, at iaculis justo pretium eget. Nullam et dui lorem. Cras vitae sem in quam pellentesque porttitor. Integer dapibus justo eget metus aliquam interdum.', '2019-01-01 00:00:00', '2019-01-01 00:00:00', 1, 1, 'instance/uploads/1/data_source_3.csv', 0, 0, 1, 1);


insert into main.data_source (title, description, created_at, published_at, is_published, type_id, data_root,
                              is_private, subscription_fee, responsible_employee, created_by)
values ('Mock Data 4', 'Aliquam commodo mauris urna, non lacinia sapien auctor et. Maecenas mattis facilisis laoreet. Quisque viverra sodales purus, vestibulum sollicitudin ex lacinia nec. Maecenas faucibus, neque quis dignissim lacinia, nisl diam rutrum lectus, ut convallis nulla erat ornare ex. Etiam feugiat tellus augue, quis dignissim orci tristique quis. Vestibulum eu egestas arcu. Vestibulum ut massa rutrum, vulputate dui vitae, imperdiet turpis.', '2019-01-01 00:00:00', '2019-01-01 00:00:00', 1, 1, 'instance/uploads/1/data_source_3.csv', 0, 0, 1, 1);

/*subscriptions*/
insert into main.subscription (subscriber, data_source, request, subscription_type, status)
values (1, 1, 1, 1, 1);

insert into main.subscription (subscriber, data_source, request, subscription_type, status)
values (1, 2, 1, 1, 1);

insert into main.subscription (subscriber, data_source, request, subscription_type, status)
values (2, 2, 1, 1, 1);

/* data source permission types and data source permissions */

insert into main.data_source_permission (data_source, employee, permission_type) values (1, 1, 'read');
insert into main.data_source_permission (data_source, employee, permission_type) values (1, 2, 'read');

