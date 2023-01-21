# sm_city

`sm_city` is our free, open-source AI solution for smart cities focuses on reducing pollution, waste & bad views. Includes matrix for maintaining cleanliness. Join our community and help make our cities better places to live.

## Technical Description

This solution works towards making it easy for cities and municipalities to detect and report street problems, such as distortions and visual pollution. The solution targets being deployed on edge devices for portability and to allow this solution to run on moving vehicles rather than on static sites.

The solution is mainly an AI model that is built with the previous requirements and goals in mind.

By evaluating several model architectures, and in terms of model efficiency, performance, and portability, we found out `efficientnet lite` architecture meets the requirements, especially the deployment target is edge devices (Power-constraint IoT devices, work with CPU with Intel XNNPACK if GPU not present, and work with Edge-TPU). With the model architecture decided, next step is to train a model on dataset that covers the street problems.

With challenges in dataset, such as inaccurate, incomplete annotations, training the model on the dataset alone is not possible, and to resolve this challenge in scalable approach, the following steps are taken:
1. Train the model with existing dataset and its annotations.
2. Evaluate the model against test data.
3. Infer data from original dataset, and save output as annotations.
4. Visualise annotated assets (from #3) and select true-positive results and discard false-positives by a human interaction.
5. Fine-tune existing model from updated annotations.
6. Test fine-tuned model with unseen data.

By executing previous steps, we found that the model has improved the annotations of the original dataset with minimum interaction from a human. Following the improvement on the model after executing the previous steps, it can be repeated until the model has reached high-level of mAP, while the human interaction becomes less with every cycle.

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

