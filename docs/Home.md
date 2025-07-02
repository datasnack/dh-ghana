# Welcome to the Demo Hub

<div class="alert alert-warning" role="alert">
This is a demo version of the Data Hub framework, developed by the Data Snack initiative at the Bernhard Nocht Institute for Tropical Medicine. The framework is under ongoing development, and this demo is not intended to serve as a fully functional data collaboration platform. Features like data downloads and API access are implemented only for demonstration purposes. For more information, visit us at <a href="https://datasnack.org">datasnack.org</a>.
</div>

<img style="max-width: 250px; min-width: 50px; width: 30%; height: auto; margin: 1rem;" src="{% static 'ghanaflag_pixelart.svg' %}" width="250" height="355" alt="" class="float-end">

## Give me a spin, I'm your Data Hub prototype in action!

The **Data Hub** serves as a dynamic spatio-temporal information platform, tailored to the data practices of researchers. It offers an integrated view of various Data Layers relevant to your study region, spanning multiple categories such as socio-demographic, environmental, weather, health, and infrastructure. These layers are compiled from user-based and open data sources (with some layers originating from the same source) to support data analysis and decision-making.

The hub currently holds {{ shapes_count }} shapes, from the following types:

<ul>
{% for type in nav_shape_types %}
<li><a href="{{ type.get_absolute_url }}">{{ type.name }}</a> ({{ type.shapes.all.count }})</li>
{% endfor %}
</ul>


<div class="alert alert-light" style="clear: right">
<b>Ghana Administrative Boundaries</b>
<p>In 2019, the number of regions increased from 10 to 16. 173 districts existed in 2010 and 216 districts in 2017. Their number has grown to 260 by splits in 2018 and 2019. Guan was inaugurated as 261st district in October 2021.</p>
<p>The geoshapefile of Ghana presented in this Data Hub is representing the map status prior October 2021. The data is sourced from Ghana Statistical Services (GSS) contributed by OCHA West and Central Africa (ROWCA) via the <a href="https://data.humdata.org/dataset/cod-ab-gha">Humanitarian Data Exchange Platform</a> (HDX).</p>
</div>


More details and in-depth documentation of each Data Layer can be accessed via its [documentation page]({% url 'datalayers:datalayer_index' %}), including metadata information.

To access the gathered open data sources you can browse them via the above-mentioned shape types or the [location picker]({% url "app:tools_picker" %}). Upon choosing your area of interest, you can tailor your data selection through our download configurator, which also offers a basic preview (spatial and temporal description) of the data for your convenience.

### Terms of Use

The {{ datahub_name }} hosts datasets under a wide range of licenses, ensuring compliance with the intellectual property rights of the various data sources utilized. Some datasets have been processed according to the needs of potential user groups. By accessing datasets through the Data Hub and/or the original source, users implicitly agree to abide by the terms of the applicable license specific to each dataset, as described in the dataset's metadata. This includes that when utilizing any data provided through the Data Hub, the data custodian shall be credited in the manner specified in the respective license and that relevant copyright provisions shall be complied with.

In addition, the Data Hub shall be cited as contributing service as follows:

{% include "app/citation.html" %}


#### Disclaimer

<div class="small">

Basic Usage Metrics Tracking - We use a self-hosted [Umami Analytics](https://umami.is/) to monitor and improve our website's performance. Umami is an open-source, privacy-focused tool that tracks basic usage metrics anonymously, without collecting any personally identifiable information (PII) or using cookies. All data is aggregated to help us understand site traffic and user interactions while respecting your privacy.

</div>
