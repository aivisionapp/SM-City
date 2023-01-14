# sm_city

`sm_city` is our free, open-source AI solution for smart cities focuses on reducing pollution, waste & bad views. Includes matrix for maintaining cleanliness. Join our community and help make our cities better places to live.

## This Repository

This repository is the workspace containing all the solution elements. It serves as `monorepo` for the project.

### Repository Projects

This repository includes following projects and elements:

1. `image_spool`: Tool to automate capturing frames from a IP camera, analysing it using the embedded AI model to identify possible labels, and `POST` it to `backend`.
2. `backend`: HTTP API that serves the following functions:
  1. Receive images and associated meta data from `image_spool` ("Data").
  2. Store Data in database for logging.
  3. Handle `frontend` requests.
3. `frontend`: Front-end to view real-time, and past logs.
4. `infrastructure`: Config files to serve the solution using Docker/Podman.
5. `assets`: Contains training materials and its annotations files.
6. `scripts`: Collection of automation and training scripts.
