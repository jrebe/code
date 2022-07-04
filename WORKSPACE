workspace(name = "code")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

################
# Golang
rules_go_version = "v0.33.0"  # latest @ 2022/06/06

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "685052b498b6ddfe562ca7a97736741d87916fe536623afb7da2824c0211c369",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/{version}/rules_go-{version}.zip".format(version = rules_go_version),
        "https://github.com/bazelbuild/rules_go/releases/download/{version}/rules_go-{version}.zip".format(version = rules_go_version),
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.16")

gazelle_version = "v0.25.0"  # latest @ 2022/03/23

# Gazelle - used for Golang external dependencies
http_archive(
    name = "bazel_gazelle",
    sha256 = "5982e5463f171da99e3bdaeff8c0f48283a7a5f396ec5282910b9e8a49c0dd7e",
    urls = [
        "https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/bazel-gazelle/releases/download/{version}/bazel-gazelle-{version}.tar.gz".format(version = gazelle_version),
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/{version}/bazel-gazelle-{version}.tar.gz".format(version = gazelle_version),
    ],
)

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

gazelle_dependencies()

load("//third_party:go_workspace.bzl", "go_dependencies")

go_dependencies()

################
# Python
rules_python_version = "0.9.0" # Latest 2022/06/09

http_archive(
    name = "rules_python",
    sha256 = "5fa3c738d33acca3b97622a13a741129f67ef43f5fdfcec63b29374cc0574c29",
    strip_prefix = "rules_python-0.9.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.9.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python39",
    # Available versions are listed in @rules_python//python:versions.bzl.
    python_version = "3.9.12",
)

load("@python39//:defs.bzl", "interpreter")

load("@rules_python//python:pip.bzl", "pip_install", "pip_parse")

pip_install(
    name = "py_deps",
    requirements = "//third_party:requirements.txt",
    python_interpreter_target = interpreter,
)

################
# Buildifier 
http_archive(
    name = "buildifier_prebuilt",
    sha256 = "c0c8a5e6caf9a99b037e77ed7a5f17615d50881d0d93de3e85c014705f7914fd",
    strip_prefix = "buildifier-prebuilt-0.4.1",
    urls = [
        "http://github.com/keith/buildifier-prebuilt/archive/0.4.1.tar.gz",
    ],
)

load("@buildifier_prebuilt//:deps.bzl", "buildifier_prebuilt_deps")

buildifier_prebuilt_deps()

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()

load("@buildifier_prebuilt//:defs.bzl", "buildifier_prebuilt_register_toolchains")

buildifier_prebuilt_register_toolchains()

################
# NodeJS

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "ee3280a7f58aa5c1caa45cb9e08cbb8f4d74300848c508374daf37314d5390d6",
    urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/5.5.1/rules_nodejs-5.5.1.tar.gz"],
)

load("@build_bazel_rules_nodejs//:repositories.bzl", "build_bazel_rules_nodejs_dependencies")

build_bazel_rules_nodejs_dependencies()

load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories")
node_repositories()

load("@build_bazel_rules_nodejs//:index.bzl", "yarn_install")

yarn_install(
    name = "npm",
    package_json = "//third_party/yarn:package.json",
    yarn_lock = "//third_party/yarn:yarn.lock",
)

################
# Distributions

vaticle_bazel_distribution_version = "e61daa787bc77d97e36df944e7223821cab309ea"  # Latest at 2022/06/14

http_archive(
    name = "vaticle_bazel_distribution",
    sha256 = "ed3444c57b51251e856326be8c323a0c3275825bfe252af410a706d9448d6fbb",
    strip_prefix = "bazel-distribution-{version}".format(version = vaticle_bazel_distribution_version),
    urls = ["https://github.com/vaticle/bazel-distribution/archive/{version}.zip".format(version = vaticle_bazel_distribution_version)],
)

pip_install(
    name = "vaticle_bazel_distribution_pip",
    requirements = "@vaticle_bazel_distribution//pip:requirements.txt",
)

load("@vaticle_bazel_distribution//pip:deps.bzl", vaticle_bazel_distribution_pip_deps = "deps")
vaticle_bazel_distribution_pip_deps()

################
# Protobufs

protobuf_version = "3.21.2" # 2022/06/23

# requirement of 'com_github_bazelbuild_buildtools'
http_archive(
    name = "com_google_protobuf",
    sha256 = "66e1156ac78290db81335c79d1fc5a54123ebb62a43eb2e5b42a44ca23087517",
    strip_prefix = "protobuf-%s" % protobuf_version,
    url = "https://github.com/protocolbuffers/protobuf/archive/v%s.tar.gz" % protobuf_version,
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

# buildifier BUILD file linter
http_archive(
    name = "com_github_bazelbuild_buildtools",
    strip_prefix = "buildtools-master",
    url = "https://github.com/bazelbuild/buildtools/archive/master.zip",
)
