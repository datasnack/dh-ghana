# Data Hub Demo for Ghana

<!-- Integration of Grey Info Box design "alert-primary" -->
<div class="alert alert-primary" role="alert">
<b>DISCLAIMER:</b> This  <b>Demo Data Hub</b>, developed by the <a href="https://datasnack.org">Data Snack initiative</a> at the <b>Bernhard Nocht Institute for Tropical Medicine</b>, offers a glimpse into our open-osurce data collaboration framework. Features like data downloads and API access are included for demonstration purposes only. The software framework is under active development. For more details, visit <a href="https://github.com/datasnack/datahub">https://github.com/datasnack/datahub</a>.
</div>

<img style="max-width: 230px; min-width: 75px; width: 30%; height: auto; margin: 1rem 0 1rem 3rem;" src="{% file 'images/ghanaflag_pixelart.svg' %}" width="100" height="184" alt="" class="float-end">

<br>

## Give me a spin, I'm your Data Hub in action!

The **Data Hub** is an open-source software framework for spatiotemporal data curation, harmonization, and collaboration — modular in design and deployable on-premise. It is tailored to the needs of Global Health research teams and integrates diverse data layers across health, demographic, socioeconomic, environmental, meteorological, and infrastructure domains, among others. Data availability, resolution, and timeliness reflect the respective original sources.
This demo instance covers the region of **Ghana** from 2020 to 2025. Ghana was chosen as a demo region due to its long-standing partnership with the *Bernhard Nocht Institute for Tropical Medicine*, which maintains the *Kumasi Centre for Collaborative Research in Tropical Medicine (KCCR)* in Kumasi.

<br>

<!-- Integration of Shapes Logo derived from external source -->
### {% icon "location" size=24 %} Shapes

[Ghana](https://en.wikipedia.org/wiki/Ghana) is a West African country bordered by Burkina Faso to the north, Togo to the east, and Côte d'Ivoire to the west, with a southern coastline along the Gulf of Guinea. The landscape transitions from coastal plains in the south through forested highlands in the center to savanna regions in the north. Population is concentrated in the southern half, particularly around the capital Accra and the inland commercial center of Kumasi.

The country is organized into **administrative units**, ranging from terrestrial plains to regions, districts and councils. <br>
The **Data Hub** currently holds {{ shapes_count }} shapes from the following types:
<ul>
{% for type in nav_shape_types %}
<li><a href="{{ type.get_absolute_url }}">{{ type.name }}</a> ({{ type.shapes.all.count }})</li>
{% endfor %}
</ul>

You can find an overview of all shapes in the [Shapes]({% url "shapes:shape_detail_all" %}) section. From there, you can explore individual spatial units and access them via API or as downloadable files for further analysis. The data originates from Ghana Statistical Service and was published via the [*Humanitarian Data Exchange Platform (HDX)*](https://data.humdata.org/dataset/cod-ab-gha) by OCHA West and Central Africa, last updated October 2021.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "stack" size=24 %} Data Layers

**Data Layers** are compiled from both user-contributed and open data sources, with some layers derived from the same source. You can browse the full catalog via the [Data Layers]({% url "datalayers:datalayer_index" %}) overview, or use the [Shapes]({% url "shapes:shape_detail_all" %}) or [Location Picker]({% url "app:tools_picker" %}) to discover all available Data Layers for a specific spatial unit of interest.

Each Data Layer can be explored in depth through a **Summary Panel** — see the [Forest land cover]({% url "datalayers:datalayer_detail" "copernicus_forest" %}) data layer as an example. The panel features interactive map previews and temporal visualizations that reveal spatial distributions and trends over time. It also includes detailed metadata covering data coverage, quality indicators, and statistical attributes. Data can be accessed via API or as downloadable files.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "tools" size=24 %} Tools

The **Tools** section hosts extensions built on the core Data Hub framework — ranging from enhanced data layer interactions to analytical pipelines and data products such as dashboards or interactive maps. One example is the [Location Picker]({% url "app:tools_picker" %}), which retrieves contextual data layers for any given coordinate — useful for example to enrich event-based surveillance or early warning systems with local context. New tools are continuously developed and shared here as open-source extensions, where relevant to the community.

<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "book" size=24 %} Docs

The **Documentation** section provides project-relevant reference material, including a [Project Summary]({% url "app:docs_page" "data-snack" %}) and auxiliary documentation such as [Use Case Overview]({% url "app:docs_page" "use-case-overview" %}), [Shapefile History]({% url "app:docs_page" "shapefile-history" %}), [Terms of Use]({% url "app:docs_page" "terms-of-use" %}), and the [Changelog]({% url "app:changelog" %}). Project teams maintain documentation as Markdown files in their project workspace (e.g., GitHub).

<br>
<br>

<!-- Integration of Data Layer Logo derived from external source -->
### {% icon "rocket" size=24 %} Found our work useful?

If you used the **Data Hub** for data processing, metadata integration, or visualization in your work, please cite it as a contributing service:
{% include "app/citation.html" %}

<br>

<!-- Integration of Grey Info Box design "alert-secondary" -->
<div class="alert alert-secondary">
<b>USAGE TRACKING: </b> We use self-hosted <a href="https://umami.is/">Umami Analytics</a> to monitor and improve our website's performance. Umami is an open-source, privacy-focused tool that tracks basic usage metrics anonymously, without collecting any personally identifiable information (PII) or using cookies. All data is aggregated to help us understand site traffic and user interactions while respecting your privacy.
</div>
