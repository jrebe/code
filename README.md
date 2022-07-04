# Monorepo

## Getting Started

### Prerequisites:
Using Ubuntu 20.04 as a base

* Install [Bazelisk](https://github.com/bazelbuild/bazelisk#installation)
* Install python3-pip (sudo apt install -y python3-pip)
* Install openjdk-17-jdk-headless (sudo apt install -y openjdk-17-jdk-headless)

## Development

### Build

`bazel build //...`

### Testing

`bazel test //...`

### Continuous Integration (CI)

This repository's CI is managed by [Buildkite](https://buildkite.com), the CI platform used by Pinterest and Canva to manage Bazel monorepos,
as well as being [used by the Bazel open-source project itself](https://buildkite.com/bazel).

### Deployment & Distribution

Deployable artifacts are pushed to S3 under commit-hash-versioned keys.
Currently only the `store-api` deploy/fat JAR is deployable.

[`vaticld/bazel-distribution`](https://github.com/graknlabs/bazel-distribution) is used to publish Python packages to PyPi. 

### Build Observability + Analysis

This project is using [Buildbuddy.IO](https://buildbuddy.io/). Every build run locally or in CI get its own `https://app.buildbuddy.io/invocation/xyz123...` URL which analyses and records the build's information.

### Linting

[thundergolfer/bazel-linting-system](https://github.com/thundergolfer/bazel-linting-system) is used. [`./tools/linting/lint.sh`](tools/linting/lint.sh) will lint all source-code in the repo and [`./tools/linting/lint_bzl_files.sh`](tools/linting/lint_bzl_files.sh) will lint all Bazel files.

