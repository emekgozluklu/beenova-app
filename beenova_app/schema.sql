
DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  company INTEGER,
  phone_number TEXT,
  is_admin INTEGER NOT NULL,
  is_company_admin INTEGER NOT NULL,
  is_activated INTEGER NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by INTEGER,
  profile_photo,
  FOREIGN KEY (company) REFERENCES company (id),
  FOREIGN KEY (created_by) REFERENCES employee (id)
);


DROP TABLE IF EXISTS company;
CREATE TABLE company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  registered_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  admin_id INTEGER NOT NULL,
  FOREIGN KEY (admin_id) REFERENCES employee (id)
);


DROP TABLE IF EXISTS data_source;
CREATE TABLE data_source (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  published_at TIMESTAMP,
  is_published INTEGER NOT NULL,
  type_id INTEGER NOT NULL,
  data_root TEXT NOT NULL,
  is_private INTEGER NOT NULL,
  subscription_fee DOUBLE,
  responsible_employee INTEGER NOT NULL,
  created_by INTEGER NOT NULL,
  FOREIGN KEY (type_id) REFERENCES data_source_type (id),
  FOREIGN KEY (responsible_employee) REFERENCES employee (id),
  FOREIGN KEY (created_by) REFERENCES employee (id)
);


DROP TABLE IF EXISTS data_usage;
CREATE TABLE data_usage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data_source INTEGER NOT NULL,
  data_user INTEGER NOT NULL,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  usage_amount DOUBLE,
  subscription INTEGER NOT NULL,
  FOREIGN KEY (data_source) REFERENCES data_source (id),
  FOREIGN KEY (data_user) REFERENCES company (id),
  FOREIGN KEY (subscription) REFERENCES subscription (id)
);


DROP TABLE IF EXISTS subscription;
CREATE TABLE subscription (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  subscriber INTEGER NOT NULL,
  data_source INTEGER NOT NULL,
  request INTEGER NOT NULL,
  subscription_started TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  subscription_ended TIMESTAMP DEFAULT NULL,
  subscription_type INTEGER NOT NULL,
  status INTEGER NOT NULL,
  FOREIGN KEY (subscriber) REFERENCES company (id),
  FOREIGN KEY (data_source) REFERENCES data_source (id),
  FOREIGN KEY (request) REFERENCES request (id)
);

DROP TABLE IF EXISTS request;
CREATE TABLE request (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  requester INTEGER NOT NULL,
  data_source INTEGER NOT NULL,
  request_message TEXT,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  date_updated TIMESTAMP DEFAULT NULL,
  status INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (requester) REFERENCES employee (id),
  FOREIGN KEY (data_source) REFERENCES data_source (id)
);


DROP TABLE IF EXISTS permission;
CREATE TABLE permission (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);


DROP TABLE IF EXISTS employee_permission;
CREATE TABLE employee_permission (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee INTEGER NOT NULL,
  permission INTEGER NOT NULL,
  FOREIGN KEY (employee) REFERENCES employee (id),
  FOREIGN KEY (permission) REFERENCES permission (id)
);
