-- Insert Master Data

INSERT INTO machines (machine_id,machine_type) VALUES ('M001','Turning'),('M002','Turning'),('M003','Turning')
,('M004','Turning'),('M005','Turning'),('M006','Turning'),('M007','Turning');

INSERT INTO operators (operator_id) VALUES ('OP001'),('OP002'),('OP003'),('OP004'),('OP005'),('OP006'),('OP007'),('OP008'),('OP009'),('OP010');

INSERT INTO work_orders (work_order_id,part_type,material) VALUES ('W001','Cone','Steel'),('W002','Pin','Steel'),('W003','Cone','Aliminium')
,('W004','Flange','Steel'),('W005','Bowl','Steel'),('W006','Flange','Steel'),('W007','Bowl','Copper'),('W008','Cone','Copper'),('W009','Bowl','Steel')
,('W010','Pin','Steel');

INSERT INTO tools (tool_id,tool_type,insert_shape,chip_breaker) VALUES ('T001','Diamond Insert','Triangular','False'),('T002','Diamond Insert','Romboid','True')
,('T003','Diamond Insert','Romboid','False'),('T004','Diamond Insert','Triangular','True'),('T005','Diamond Insert','Romboid','False')
,('T006','Diamond Insert','Romboid','False'),('T007','Diamond Insert','Romboid','False'),('T008','Diamond Insert','Triangular','True')
,('T009','Diamond Insert','Triangular','False'),('T010','Diamond Insert','Romboid','True');

INSERT INTO tool_positions (position_id, tool_id, position_number)
VALUES('P001', 'T001', 1),('P002', 'T001', 2),('P003', 'T001', 3),('P004', 'T002', 1),('P005', 'T002', 2),('P006', 'T002', 3),('P007', 'T002', 4)
,('P008', 'T003', 1),('P009', 'T003', 2),('P010', 'T003', 3),('P011', 'T003', 4),('P012', 'T004', 1),('P013', 'T004', 2),('P014', 'T004', 3)
,('P015', 'T005', 1),('P016', 'T005', 2),('P017', 'T005', 3),('P018', 'T005', 4),('P019', 'T006', 1),('P020', 'T006', 2),('P021', 'T006', 3)
,('P022', 'T006', 4),('P023', 'T007', 1),('P024', 'T007', 2),('P025', 'T007', 3),('P026', 'T007', 4),('P027', 'T008', 1),('P028', 'T008', 2)
,('P029', 'T008', 3),('P030', 'T009', 1),('P031', 'T009', 2),('P032', 'T009', 3),('P033', 'T010', 1),('P034', 'T010', 2),('P035', 'T010', 3)
,('P036', 'T010', 4);





