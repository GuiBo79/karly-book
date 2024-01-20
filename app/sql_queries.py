SUMMARY_INCIDENTS = """
CREATE VIEW summary_incidents AS
SELECT
    `fire_incidents_data`.neighborhood_district,
    COUNT(*) AS total_incidents
FROM
    `fire_incidents_data`
GROUP BY
    neighborhood_district
ORDER BY
    total_incidents
DESC;
"""

INCIDENTS_DETAILS = """
CREATE VIEW grave_incidents_details AS
SELECT 
    incident_number,
    address,
    incident_date,
    estimated_property_loss,
    fire_fatalities,
    fire_injuries,
    civilian_fatalities,
    civilian_injuries
FROM 
    `fire_incidents_data`
WHERE 
    fire_fatalities > 0 OR 
    fire_injuries > 0 OR 
    civilian_fatalities > 0 OR 
    civilian_injuries > 0 OR 
    estimated_property_loss > 1;
"""
