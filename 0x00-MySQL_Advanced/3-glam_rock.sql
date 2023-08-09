--  lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name,
       FLOOR(DATEDIFF('2022-01-01', formed) / 365) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
