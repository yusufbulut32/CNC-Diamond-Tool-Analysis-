--Create Database Tables

CREATE TABLE machines (
    machine_id VARCHAR(10) PRIMARY KEY,
    machine_type VARCHAR(30)
);

CREATE TABLE operators (
    operator_id VARCHAR(10) PRIMARY KEY
);

CREATE TABLE work_orders (
    work_order_id VARCHAR(20) PRIMARY KEY,
    part_type VARCHAR(50),
    material VARCHAR(30)
);

CREATE TABLE tools (
    tool_id VARCHAR(10) PRIMARY KEY,
    tool_type VARCHAR(50),
    insert_shape VARCHAR(10),
    chip_breaker BOOLEAN,
    wiper BOOLEAN
);

CREATE TABLE tool_positions (
    position_id VARCHAR(10) PRIMARY KEY,
    tool_id VARCHAR(10),
    position_number INT,
    FOREIGN KEY (tool_id) REFERENCES tools(tool_id),
    UNIQUE (tool_id, position_number),
    CHECK (position_number BETWEEN 1 AND 4)
);

CREATE TABLE operations (
    operation_id VARCHAR(10) PRIMARY KEY,
    work_order_id VARCHAR(20),
    machine_id VARCHAR(10),
    operator_id VARCHAR(10),
    parts INT,
    cutting_time DECIMAL(8,2),
    rpm INT,
    FOREIGN KEY (work_order_id) REFERENCES work_orders(work_order_id),
    FOREIGN KEY (machine_id) REFERENCES machines(machine_id),
    FOREIGN KEY (operator_id) REFERENCES operators(operator_id)
);

CREATE TABLE operation_tools (
    operation_id VARCHAR(10),
    tool_id VARCHAR(10),
    PRIMARY KEY (operation_id, tool_id),
    FOREIGN KEY (operation_id) REFERENCES operations(operation_id),
    FOREIGN KEY (tool_id) REFERENCES tools(tool_id)
);

CREATE TABLE wear_measurements (
    measurement_id SERIAL PRIMARY KEY,
    position_id VARCHAR(10),
    operation_id VARCHAR(10),
    wear_mm DECIMAL(6,3),
    visual_condition VARCHAR(30),
    measurement_date DATE,
    FOREIGN KEY (position_id) REFERENCES tool_positions(position_id),
    FOREIGN KEY (operation_id) REFERENCES operations(operation_id)
);