# Code Monorepo

## Getting Started

### Prerequisites:
Using Ubuntu 20.04 as a base

* Install [Bazelisk](https://github.com/bazelbuild/bazelisk#installation)
* Install python3-pip (sudo apt install -y python3-pip)

## Development

### Build

`bazel build //...`

### Testing

`bazel test //...`

## Dependencies

Each language has its own import requirements.

### Python

Add the new sorted requirements to `third_party/requirements.in` and run `bazel run //third_party:requirements.update`

