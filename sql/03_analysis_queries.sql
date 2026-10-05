-- Tool Wear Analysis

-- 1. Average wear by tool

SELECT
    tp.tool_id,
    COUNT(*) AS measurement_count,
    AVG(wm.wear_mm) AS avg_wear,
    MAX(wm.wear_mm) AS max_wear
FROM wear_measurements wm
JOIN tool_positions tp
    ON wm.position_id = tp.position_id
GROUP BY tp.tool_id
ORDER BY avg_wear DESC;

-- 2. Wear Status by tool

SELECT
    tp.tool_id,
    wm.measurement_id,
    wm.wear_mm,
    CASE
        WHEN wm.wear_mm < 0.10 THEN 'Normal'
        WHEN wm.wear_mm < 0.20 THEN 'Monitor'
        ELSE 'Replacement Recommend'
    END AS wear_status
FROM wear_measurements wm
JOIN tool_positions tp
    ON wm.position_id = tp.position_id
ORDER BY wm.wear_mm DESC;

-- 3. Average wear by material

SELECT
    wo.material,
    COUNT(*) AS measurement_count,
    AVG(wm.wear_mm) AS avg_wear
FROM wear_measurements wm
JOIN operations o
    ON wm.operation_id = o.operation_id
JOIN work_orders wo
    ON o.work_order_id = wo.work_order_id
GROUP BY wo.material
ORDER BY avg_wear DESC;
