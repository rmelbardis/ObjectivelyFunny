# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr ObjectivelyFunny-*.dist-info
	@rm -fr ObjectivelyFunny.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)

# ------------------------------------
#      GOOGLE CLOUD RUNNING / STORAGE
# ------------------------------------

JAMES_PROJECT_ID=le-wagon-data-342210
JAMES_BUCKET_NAME= wagon-data-805-farrell
REGION=europe-west1

set_project:
	@gcloud config set project ${PROJECT_ID}

##### Python params  - - - - - - - - - - - - - - - - - - -
PYTHON_VERSION=3.7
FRAMEWORK=scikit-learn
RUNTIME_VERSION=2.8

##### Package params  - - - - - - - - - - - - - - - - - - -

PACKAGE_NAME=ObjectivelyFunny
FILENAME=gpt2_trainer

##### Job - - - - - - - - - - - - - - - - - - - - - - - - -

JOB_NAME=comedy_model_training_$(shell date +'%Y%m%d_%H%M%S')

##### Bucket - - - - - - - -
BUCKET_TRAINING_FOLDER = 'gpt2-trainings'

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/${BUCKET_TRAINING_FOLDER} \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION} \
		--stream-logs \
		--scale-tier CUSTOM \
		--master-machine-type n1-standard-16



#adding credentials manually
credentials:
	export GOOGLE_APPLICATION_CREDENTIALS='/home/jfazz9/code/jfazz9/gcp/le-wagon-data-342210-aeff00e67628.json'
