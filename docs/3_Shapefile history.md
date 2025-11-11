---
title: Shapefile history
---

# Shapefile history

[Ghana](https://en.wikipedia.org/wiki/Ghana) is a West African country bordered by Burkina Faso to the north, Togo to the east, and Côte d'Ivoire to the west, with a southern coastline along the Gulf of Guinea. The landscape transitions from coastal plains in the south through forested highlands in the center to northern savanna regions. Most of the population is concentrated in the southern half, particularly around the capital Accra on the coast and the inland commercial center of Kumasi.

<br>

### Shapefile Ghana

The country Ghana is organized into administrative units, ranging from terrestrial plains to regions, districts and councils. The geoshapefile of Ghana presented in this Data Hub is representing the map status **prior October 2021**.

The **Data Hub** currently holds {{ shapes_count }} shapes from the following types:

<ul>
{% for type in nav_shape_types %}
<li><a href="{{ type.get_absolute_url }}">{{ type.name }}</a> ({{ type.shapes.all.count }})</li>
{% endfor %}
</ul>

The data is sourced from *Ghana Statistical Services* contributed by *OCHA West and Central Africa* via the [*Humanitarian Data Exchange Platform (HDX)*](https://data.humdata.org/dataset/cod-ab-gha).

<br>

### Identifiers of spatial units

The `keys` assigned to each spatial unit in our **Demo Data Hub** follow the [p-code](https://humanitarian.atlassian.net/wiki/spaces/imtoolbox/pages/222265609/P-codes) (place codes) structure, in line with the standard geographic references adopted by the humanitarian community and provided by [*UN OCHA*](https://www.unocha.org/).

P-codes are unique geographic identifiers - typically alphanumeric - that designate specific places, points, positions, or features on a map or within a database. Each administrative unit is assigned exactly one p-code, reflecting a hierarchical structure in which lower-level codes incorporate those of higher-level units. A global list of p-codes is available via the the [*Humanitarian Data Exchange Platform*](https://data.humdata.org/dataset/global-pcodes).

Within national reference systems, unique identifiers may differ from the p-code. As such, the p-code should be regarded as a recommendation and as part of an international reference framework.

<br>


### Ghana administrative devisions under development

In 2019, the number of regions in Ghana increased from 10 to 16. 173 districts existed in 2010 and 216 districts in 2017. Their number has grown to 260 by splits in 2018 and 2019. Guan was inaugurated as the 261st district in October 2021.


{% icon "hourglass" size=16 %} More detailed description coming soon...

<br>
<br>