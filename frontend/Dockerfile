#Stage 1 - Install dependencies and build the app in a build environment
# Install flutter dependencies
FROM debian:latest AS build-env
RUN apt-get update
RUN apt-get install -y curl git wget unzip libgconf-2-4 gdb libstdc++6 libglu1-mesa fonts-droid-fallback lib32stdc++6 python3 sed
# Clone the flutter repo
RUN apt-get clean
# Set flutter path
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter
# Run flutter doctor
ENV TAR_OPTIONS="--no-same-owner"
ENV PATH="${PATH}:/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin"
RUN flutter channel stable
RUN flutter doctor -v
# Copy files to container and build
RUN flutter upgrade
RUN mkdir /app/
COPY . /app/
# Stage 2 - Create the run-time image
WORKDIR /app
RUN flutter build web
FROM nginx:1.21.1-alpine
COPY --from=build-env /app/build/web /usr/share/nginx/html

