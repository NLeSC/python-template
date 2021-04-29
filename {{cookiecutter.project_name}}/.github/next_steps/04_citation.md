---
title: 'Next step: Citation data'
---

It is likely that your `CITATION.cff` currently doesn't pass validation. The error messages you get from the [`cffconvert`]({{cookiecutter.repository}}/actions/workflows/cffconvert.yml) GitHub Action are unfortunately a bit cryptic, but doing the following helps:

- [ ] Check if the `given-name` and `family-name` keys need updating. If your family name has a name particle like `von` or `van` or `de`, use the `name-particle` key; if your name has a suffix like `Sr` or `IV`, use `name-suffix`. For details, refer to the schema description: https://github.com/citation-file-format/citation-file-format
- [ ] Update the value of the `orcid` key. If you do not have an orcid yet, you can get one here [https://orcid.org/](https://orcid.org/).
- [ ] Add more authors if needed
- [ ] Update `date-released` using the YYYY-MM-DD format.
- [ ] Update the `doi` key with the conceptDOI for your repository (see [https://help.zenodo.org](https://help.zenodo.org/) for more information on what a conceptDOI is). If your project doesn't have a DOI yet, you can use the string `10.0000/FIXME` to pass validation.
- [ ] Update the `keywords` array with some keywords of your own that describe your project.

Once you do all the steps above, the `cffconvert` workflow will tell you what content it expected to see in `.zenodo.json`. Copy-paste from the GitHub Action log into a new file `.zenodo.json`. Afterwards, the `cffconvert` GitHub Action should be green.


To help you keep the citation metadata up to date and synchronized, the [`cffconvert`]({{cookiecutter.repository}}/actions/workflows/cffconvert.yml) GitHub Action checks the following 6 aspects:

1. Whether your repository includes a `CITATION.cff` file.

    _By including this file, authors of the software can receive credit for the work they put in._

1. Whether your `CITATION.cff` is valid YAML.

    _Visit https://yamllint.com to see if the contents of your CITATION.cff are valid YAML._

1. Whether your `CITATION.cff` adheres to the schema (as listed in the `CITATION.cff` file itself under key `cff-version`).

    _The Citation File Format schema can be found [here](https://github.com/citation-file-format/citation-file-format), along with an explanation of all the keys. You're advised to use the latest available schema version._

1. Whether your repository includes a `.zenodo.json` file.

    _With this file, you can control what metadata should be associated with any future releases of your software on Zenodo: things like the author names, along with their affiliations and their ORCIDs, the license under which the software has been released, as well as the name of your software and a short description. If your repository doesn't have a .zenodo.json file, Zenodo will take a somewhat crude guess to assign these metadata._

    _The `cffconvert` GitHub action will tell you what it expects to find in `.zenodo.json`, just copy and paste it to a new file named `.zenodo.json`. The suggested text ignores CITATION.cff's `version`, `commit`, and `date-released`. `cffconvert` considers these keys `suspect` in the sense that they are often out of date, and there is little purpose to telling Zenodo about these properties: Zenodo already knows._

1. Whether `.zenodo.json` is valid JSON.

    _Currently unimplemented, but you can check for yourself on [https://jsonlint.com/](https://jsonlint.com/)._ 

1. Whether `CITATION.cff` and `.zenodo.json` contain equivalent data.

    _This final check verifies that the two files are in sync. The check ignores CITATION.cff's `version`, `commit`, and `date-released`._
