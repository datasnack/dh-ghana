# DEMO Data Hub Ghana

<!-- Integration of Grey Info Box design "alert alert-warning" -->
<div class="alert alert-warning" role="alert">
<b>Disclaimer:</b> This  <b>Demo Data Hub</b>, developed by the <a href="https://datasnack.org">Data Snack initiative</a> at the <b>Bernhard Nocht Institute for Tropical Medicine</b>, offers a glimpse into our data collaboration framework. Features like data downloads and API access are included for demonstration purposes only. The framework itself is under active development. For more details, visit <a href="https://github.com/datasnack/datahub">https://github.com/datasnack/datahub</a>.
</div>

<img style="max-width: 230px; min-width: 75px; width: 30%; height: auto; margin: 1rem 0 1rem 3rem;" src="{% file 'images/ghanaflag_pixelart.svg' %}" width="100" height="184" alt="" class="float-end">

<br>

## Give me a spin, I'm your Data Hub in action!

Designed as a dynamic spatiotemporal information system, the **Data Hub** framework supports data curation, harmonization, and collaboration across domains and data-driven use cases — modular in design, open source, and locally deployable. Tailored to the needs of Global Health teams, the platform integrates diverse data layers from the demo region of **Ghana** from 1901 up to 2025, including demographic, socioeconomic, environmental, meteorological, health, and infrastructure data. Availability, resolution, and timeliness of data vary according to the original data sources. **Ghana** was chosen as a demo region due to its long-standing partnership with the *Bernhard Nocht Institute for Tropical Medicine*, which maintains the *Kumasi Centre for Collaborative Research in Tropical Medicine (KCCR)* in Kumasi.

<br>

<!-- Integration of Shapes Logo derived from external source -->
### {% icon "location" size=24 %} Shapes

[Ghana](https://en.wikipedia.org/wiki/Ghana) is a West African country bordered by Burkina Faso to the north, Togo to the east, and Côte d'Ivoire to the west, with a southern coastline along the Gulf of Guinea. The landscape transitions from coastal plains in the south through forested highlands in the center to northern savanna regions. Most of the population is concentrated in the southern half, particularly around the capital Accra on the coast and the inland commercial center of Kumasi.

The country is organized into administrative units, ranging from terrestrial plains to regions, districts and councils. The **Data Hub** currently holds {{ shapes_count }} shapes from the following types:

<ul>
{% for type in nav_shape_types %}
<li><a href="{{ type.get_absolute_url }}">{{ type.name }}</a> ({{ type.shapes.all.count }})</li>
{% endfor %}
</ul>

You can find an overview of all shapes in the [Shapes]({% url "shapes:shape_detail_all" %}) section. From there, you can explore individual spatial units and access them either via API or as downloadable files for further analysis. The data originates from *Ghana Statistical Services* and was contributed by *OCHA West and Central Africa* via [*Humanitarian Data Exchange Platform (HDX)*](https://data.humdata.org/dataset/cod-ab-gha), current as of before October 2021.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "stack" size=24 %} Data Layers

Data Layers are compiled from both user-contributed and open data sources, with some layers derived from the same source. To access Data Layers, you can browse the full catalog via the [Data Layers]({% url "datalayers:datalayer_index" %}) overview, or use the [Shapes]({% url "shapes:shape_detail_all" %}) or [Location Picker]({% url "app:tools_picker" %}) to discover all available Data Layers for a specific spatial unit of interest.

Each Data Layer can be explored in-depth through a summary panel, see example [Forest land cover]({% url "datalayers:datalayer_detail" "copernicus_forest" %}). The panel features interactive map previews and temporal visualization that reveal spatial distributions and trends over time. It further includes detailed metadata, allowing you to examine data coverage, quality indicators, and key statistical attributes before proceeding with analysis. Data can be accessed either via API or as downloadable files.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "tools" size=24 %} Tools

In the **Tools** section, you'll find extensions built on the core Data Hub framework — for example, to enhance interaction with data layers or integrate analytical pipelines. It can also host data products such as dashboards or interactive maps. One example is the [Location Picker]({% url "app:tools_picker" %}), which links contextual data from spatial units to specific coordinates, for instance, to support event-based surveillance or early warning systems. We continuously develop new tools and share them here as open source extensions, where relevant to the community.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "book" size=24 %} Docs

The **Data Hub**'s **Documentation** section collects project-relevant overviews, including a [Data Snack summary]({% url "app:docs_page" "data-snack" %}) with key project details and important documentation on topics such as the [Data Hub ecosystem]({% url "app:docs_page" "shapefile-history" %}), [Shapefile history]({% url "app:docs_page" "shapefile-history" %}), [Terms of use]({% url "app:docs_page" "terms-of-use" %}) or the [Data Hub Changelog]({% url "app:changelog" %}). Project teams can maintain all sections as Markdown files in the connected project workspace, like GitHub.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "rocket" size=24 %} Found our work useful?

If you used the **Data Hub** for data processing, metadata integration, or visualization in your work, please cite it as a contributing service using the following format:
{% include "app/citation.html" %}

<br>
<br>

<!-- Integration of Grey Info Box design "alert-secondary" -->
<div class="alert alert-secondary">
<b>Usage Metrics Tracking: </b> We use a self-hosted <a href="https://umami.is/">Umami Analytics</a> to monitor and improve our website's performance. Umami is an open-source, privacy-focused tool that tracks basic usage metrics anonymously, without collecting any personally identifiable information (PII) or using cookies. All data is aggregated to help us understand site traffic and user interactions while respecting your privacy.
</div>
