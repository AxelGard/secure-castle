# secure-castle

A python flask file server that stores files securely with encryption


[![Open this project in Cloud
Shell](http://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/AxelGard/secure-castle)

<div style="width:150px; height:100px">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fe%2Fe8%2FThe_Fortress_of_K%25C3%25B6nigstein_from_the_North_by_Bernardo_Bellotto.jpg&f=1&nofb=1"
     width="500" height="300"
     style="float: left; margin-right: 10px;" />
</div>

The Fortress of Königstein from the north by Bernardo Bellotto

## latest patch

#### secure-castle alpha.1

Now you can use secure-castle and upload file and encrypt those file.
When you want the file you can download the file and the encrypted file will be deleted.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install

```
virtualenv
python 3
```

### Installing

On macOS and Linux:

```
python3 -m pip3 install --user virtualenv
python3 -m venv env
source env/bin/activate
./install.sh
```

you can now deploy

```
./run.sh
```

### Coding style

the code style is using [pep8](https://pep8.org/)

## Deployment

for know you can just run the **run.sh** for deploying the program.

the file just **runs** the main.py file.

```
source env/bin/activate
./run.sh
```

## Built With

* [Python](https://www.python.org/) - language
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - framework
* [pyAesCrypt](https://pypi.org/project/pyAesCrypt/) - encryption lib

## Versioning

this code is just a side project i will some day make branch or tag with a stable release but for now there are not a stable version.

## Authors

* **Axel Gard** - *Initial work* - [AxelGard](https://github.com/AxelGard)

See also the list of [contributors](https://github.com/AxelGard/secure-castle/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


## Acknowledgments

* [pyAesCrypt](https://pypi.org/project/pyAesCrypt/)
*
