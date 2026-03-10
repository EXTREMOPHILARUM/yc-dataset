# Launches

## Mundi 🗺️ The Open Source GIS Built for AI

# Mundi, the first open source, AI-native GIS

Mundi is an open source web GIS built to help people use LLMs in their geospatial work. In Mundi, you collaborate with Kue, our AI GIS agent, to edit your map, rather than physically interacting with tools as you would in a legacy GIS.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91491&key=user_uploads/786838/49388e35-2edf-4711-8aa7-f22aed832b08)

# Here’s how Mundi is bringing AI to GIS:

**Mundi makes PostGIS much more accessible 📂** \
\
When you connect a PostGIS database to your project, Kue digests it and builds you a wiki to better understand its contents and how everything relates together. Then, if you want to add some data, all you have to do is tell Kue what data you want and it will figure out what is best and add it to your project.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91491&key=user_uploads/786838/585270c1-b025-4ebf-953d-09a0aef2417f)

\
**You can run QGIS geoprocessing in the cloud ⚙️**\
\
Kue has access to all of the QGIS geoprocessing algorithms so you get the power of a desktop GIS with the power of cloud processing. All you have to do is tell Kue what you want done with your data and it will pick the right geoprocessing algorithm, run it, and give you the output. And, because it’s run in the cloud, it’s much faster and does not need a powerful computer.\
\
**Mundi can edit symbology for you 🎨** \
\
Kue has the ability to change the symbology of your data in any way you want. If you have a specific request, it can handle it for you. Or, if you want Kue to decide how a layer should be styled, we’ve given it the ability to “see” symbology and iterate on what to improve. So, if you have a drought layer, Kue can understand that it should be a red gradient, see how it’s styled, and make improvements until Kue is satisfied.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91491&key=user_uploads/786838/7074999f-e6f5-42f0-9516-b5d07e176e94)

**You can work with your whole team on Mundi 🤝** \
\
We’re building Mundi to allow you to edit maps with your whole team and send viewable links to anyone who wants to see it. Since we built Mundi to make it easier for anyone to make maps, we wanted to make it easy for all these new mappers to work together.

**We’ve made it open source 🐧** \
\
In addition to hosted Mundi, we’re launching an open source version. If you want to try out AI locally or change Mundi to your exact needs (an exciting trend we saw at the QGIS user conference), we wanted to be sure that this was an option.

### How to try mundi:

You can sign up for Mundi at [app.mundi.ai](http://app.mundi.ai) and read the docs at [docs.mundi.ai](http://docs.mundi.ai)!

If you want to see the open source version, you can find it here: https://github.com/BuntingLabs/mundi.ai

## Bunting Labs 🐦 No-code geospatial data pipelines

**TL;DR Bunting helps developers import, store, and analyze geospatial data. We replace months of writing Python scripts with our drag-and-drop data importer.**

Hi everyone! [Brendan](https://www.linkedin.com/in/brendanashworth/) and [Michael](https://www.linkedin.com/in/michael-egan-4941a4145/) here to introduce [Bunting Labs](https://buntinglabs.com).

🗺 **Problem**

If you want to implement spatial data into your software, you need to use a spatial database. But, because spatial data is heterogenous, creating the ETL scripts, cloud infrastructure, and analysis pipelines to use it takes months—something we saw ourselves.

We spent a year trying to analyze real estate with AI, and the first three months were dedicated to building these data pipelines. We realized every company that wants to use spatial databases suffers from the same problems.

**🔧 Solution**

We handle the pipeline and the database for you. Behind the scenes we do all the leg work to work with spatial data so you can focus on building your product. For example, we automatically [convert addresses in CSVs into a PostGIS table via geocoding](https://buntinglabs.com/flows/import-csv-geocode-into-postgis). Here’s how managing spatial data on bunting would look like for you:

1. Upload any data file, and we’ll automatically recognize how it relates to the Earth. We currently support [KML](https://buntinglabs.com/flows/import-csv-geocode-into-postgis), [CSV](https://buntinglabs.com/flows/import-csv-geocode-into-postgis), [GeoJSON](https://buntinglabs.com/flows/importing-geojson-files-into-postgis), [GeoPackage](https://buntinglabs.com/flows/upload-geopackage-contents-to-postgis), and [Excel](https://buntinglabs.com/flows/load-excel-file-into-postgis).
2. We’ll save it to a managed PostGIS instance (on Amazon RDS) and give you SELECT permissions to your tables.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65769&key=user_uploads/786838/6daa1005-b597-472c-90ad-b16067886c47)

Coming soon: low-code spatial analysis tool and purpose-built spatial data labeling. Everything you need to build an app with spatial data.

**👉 Ask**

Do you work with spatial data and are willing to share your experiences? Shoot us an email at [founders@buntinglabs.com](mailto:founders@buntinglabs.com), we would love to talk.

Do you work at a company that is working on implementing or wants to implement any spatial features? Email us at [founders@buntinglabs.com](mailto:founders@buntinglabs.com), we would love to work with you to do whatever it takes to make your vision a reality!

**💻 Open Source**

Bunting is built on open source and sponsors development of [mundipy, a Python framework for geospatial data](https://docs.mundi.ai/).
