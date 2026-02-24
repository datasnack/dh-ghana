---
title: Use Case Overview
---

# Use Case Overview (Demo Template)

<br>

<!-- Integration of Grey Info Box design "alert-primary" -->
<div class="alert alert-primary" role="alert">
<b>NOTE:</b> This <b>Use Case Summary</b> serves as a template for documenting research workflows. As an example - dengue outbreak risk assessment in Ghana - this <i>Markdown</i>-based approach enables teams to collaboratively define data requirements, harmonization strategies, and analysis plans. This example is illustrative and not validated. Looking ahead, we aims to integrate automated documentation tools that generate summaries directly from curated metadata, reducing manual effort and ensuring consistency across use cases. </div>

<br>

### 1. Use Case Specification

| | |
|-------------|-----------|
|**Disease under study**|Arboviral diseases|
|**Spatial coverage**|Ghana (GHA)|
|Highest-level shape|Country (admin0)|
|Lowest-level|District (admin2)|
|Resolution appicable to use case|Region (admin1)|
|**Temporal coverage**|2020-01-01 - 2025-12-31|
|Highest-level|Year|
|Lowest-level|Day|
|Resolution appicable to use case|Month|
|**Maintenance & Updates**|  |
|Update frequency| [e.g., ad-hoc / weekly / monthly / annually]|
|Responsible|[Team member(s)]|

<br>

### 2. Data Requirements

<!-- Integration of Grey Info Box design "alert-secondary" -->
<div class="alert alert-secondary">
<b>Original data shall be uploaded here:</b>

Link: [URL]
- Avoid pre-processing original data to match use-case resolution. Instead, provide data at its native resolution. The Data Hub handles aggregation and harmonization automatically, allowing us to apply different strategies depending on the use case
- Do not clean your datasets for spatial boundary changes; document any changes you encounter instead (to be added in the Data Layer metadata). The Data Hub is developing centralized handling for spatial mismatches across all layers, so these issues can be addressed consistently platform-wide
</div>

| Data Requirements | Spatial smallest | Temporal smalltest | Study Data | Open Data |
|-------------------|------------------|--------------------|------------| ----------|
||||||
| ***EPIDEMIOLOGICAL DATA*** | *NO identifiable/sensitive data!* | | | |
| Dengue cases | {% dl_spatial "litdata_denv_lim2025" "last" %} | {% dl_temporal "litdata_denv_lim2025" "text" %} | collection ongoing | {% dl_link "litdata_denv_lim2025" %} |
| Dengue transmission suitability | {% dl_spatial "litmod_dcz_lim2025" "last" %} | {% dl_temporal "litmod_dcz_lim2025" "text" %} | -- | {% dl_link "litmod_dcz_lim2025" %} |
| Aedes-borne virus transmission suitability | {% dl_spatial "litmod_denv_lim2025" "last" %} | {% dl_temporal "litmod_denv_lim2025" "text" %} | -- | {% dl_link "litmod_denv_lim2025" %} |
||||||
| ***DEMOGRAPHIC & SOCIO-ECONOMIC*** |  |  |  |  |
| Population count | {% dl_spatial "worldpop_popc" "last" %} | {% dl_temporal "worldpop_popc" "text" %} | -- | {% dl_link "worldpop_popc" %} |
| Population density | {% dl_spatial "worldpop_popd" "last" %} | {% dl_temporal "worldpop_popd" "text" %} | -- | {% dl_link "worldpop_popd" %} |
| Wealth index (Gini) | {% dl_spatial "dhs_gini" "last" %} | {% dl_temporal "dhs_gini" "text" %} | -- | {% dl_link "dhs_gini" %} |
||||||
| ***ANIMAL DATA*** | *NO identifiable/sensitive data!* | | | |
| Livestock density cattle | {% dl_spatial "fao_livestock_cattle" "last" %} | {% dl_temporal "fao_livestock_cattle" "text" %} | -- | {% dl_link "fao_livestock_cattle" %} |
| Livestock density sheep | {% dl_spatial "fao_livestock_sheep" "last" %} | {% dl_temporal "fao_livestock_sheep" "text" %} | -- | {% dl_link "fao_livestock_sheep" %} |
| Livestock density goat | {% dl_spatial "fao_livestock_goat" "last" %} | {% dl_temporal "fao_livestock_goat" "text" %} | -- | {% dl_link "fao_livestock_goat" %} |
||||||
| ***ENTOMOLOGICAL DATA*** | | | | |
| *Aedes aegypti* abundance | -- | -- | -- | under review |
||||||
| ***WEATHER AND CLIMATIC DATA*** | |  |  |  |
| Temperature max (EO) | {% dl_spatial "era5_tmax" "last" %} | {% dl_temporal "era5_tmax" "text" %} | -- | {% dl_link "era5_tmax" %} |
| Temperature max (station) | {% dl_spatial "meteo_tmax" "last" %} | {% dl_temporal "meteo_tmax" "text" %} | -- | {% dl_link "meteo_tmax" %} |
| Temperature min (EO) | {% dl_spatial "era5_tmin" "last" %} | {% dl_temporal "era5_tmin" "text" %} | -- | {% dl_link "era5_tmin" %} |
| Temperature min (station) | {% dl_spatial "meteo_tmin" "last" %} | {% dl_temporal "meteo_tmin" "text" %} | -- | {% dl_link "meteo_tmin" %} |
| Temperature mean (EO) | {% dl_spatial "era5_tavg" "last" %} | {% dl_temporal "era5_tavg" "text" %} | -- | {% dl_link "era5_tavg" %} |
| Temperature mean (station) | {% dl_spatial "meteo_tavg" "last" %} | {% dl_temporal "meteo_tavg" "text" %} | -- | {% dl_link "meteo_tavg" %} |
| Precipitation sum (EO) | {% dl_spatial "era5_prcp" "last" %} | {% dl_temporal "era5_prcp" "text" %} | -- | {% dl_link "era5_prcp" %} |
| Precipitation sum (station) | {% dl_spatial "meteo_prcp" "last" %} | {% dl_temporal "meteo_prcp" "text" %} | -- | {% dl_link "meteo_prcp" %} |
| ENSO seasons | -- | -- | -- | under review |
||||||
| ***ENVIRONMENTAL DATA*** |  |  |  |  |
| Geographic area | -- | -- | -- | under review |
| Elevation | {% dl_spatial "worldpop_elevation" "last" %} | {% dl_temporal "worldpop_elevation" "text" %} | -- | {% dl_link "worldpop_elevation" %} |
| Urban land cover | {% dl_spatial "copernicus_built" "last" %} | {% dl_temporal "copernicus_built" "text" %} | -- | {% dl_link "copernicus_built" %} |
| Forest land cover | {% dl_spatial "copernicus_forest" "last" %} | {% dl_temporal "copernicus_forest" "text" %} | -- | {% dl_link "copernicus_forest" %} |
| Cropland land cover | {% dl_spatial "copernicus_crop" "last" %} | {% dl_temporal "copernicus_crop" "text" %} | -- | {% dl_link "copernicus_crop" %} |
| Water bodies land cover | {% dl_spatial "copernicus_water" "last" %} | {% dl_temporal "copernicus_water" "text" %} | -- | {% dl_link "copernicus_water" %} |
||||||
| ***INFRASTRUCTURE*** |  |  |  |  |
| Health facilities | {% dl_spatial "healthsitesio_facilities" "last" %} | {% dl_temporal "healthsitesio_facilities" "text" %} | -- | {% dl_link "healthsitesio_facilities" %} |
| Travel time to nearest health facility | {% dl_spatial "malariaatlas_traveltimehc" "last" %} | {% dl_temporal "malariaatlas_traveltimehc" "text" %} | -- | {% dl_link "malariaatlas_traveltimehc" %} |
| Hospital bed capacity | {% dl_spatial "who_physdens" "last" %} | {% dl_temporal "who_physdens" "text" %} | -- | {% dl_link "who_physdens" %} |
| Physicians capacity | {% dl_spatial "who_hospbeddens" "last" %} | {% dl_temporal "who_hospbeddens" "text" %} | -- | {% dl_link "who_hospbeddens" %} |
| Nurses and midwifes capacity | {% dl_spatial "who_nursmidwdens" "last" %} | {% dl_temporal "who_nursmidwdens" "text" %} | -- | {% dl_link "who_nursmidwdens" %} |

<br>

### 3. Access Methods

| | |
|-------------|-----------|
| **Shapefiles** | |
| API | template available for Python and R |
| Downloables | GeoPackage, GeoJSON, CSV (WKT) |
| **Data Layers** | |
| API | template available for Python and R |
| Downloables | CVS, Excel |

<br>