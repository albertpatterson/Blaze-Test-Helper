ts_devserver(
    name = "devserver",
    port = 4200,
    entry_module = "project/src/main.dev",
    serving_path = "/bundle.min.js",
    scripts = [
        "@npm//node_modules/tslib:tslib.js",
        ":rxjs_umd_modules",
    ],
    static_files = [
        "@npm//node_modules/zone.js:dist/zone.min.js",
    ],
    data = [
        "favicon.ico",
        "@npm//node_modules/moment:min/moment.min.js",
    ],
    index_html = "index.html",
    deps = [
      ":require.config.js",
      ":src",
    ],
)

ng_module(
    name = "src",
    srcs = glob(
        include = ["**/*.ts"],
        exclude = [
            "**/*.spec.ts",
            "main.ts",
            "test.ts",
            "initialize_testbed.ts",
        ],
    ),
    assets = glob([
      "**/*.css",
      "**/*.html",
    ]) + ([":styles"] if len(glob(["**/*.scss"])) else []),
    deps = [
        "@npm//@angular/core",
        "@npm//@angular/platform-browser",
        "@npm//@angular/router",
        "@npm//@types",
        "@npm//rxjs",
    ],
)

karma_web_test_suite(
    deps = [
        "@npm//@angular/core",
        "@npm//@angular/platform-browser",
        "@npm//@angular/router",
        "@npm//@types",
        "@npm//rxjs",
    ]
        name = 'test11'
)


karma_web_test_suite(
    name="test22"
    deps = [
        "@npm//@angular/core",
        "@npm//@angular/platform-browser",
        "@npm//@angular/router",
        "@npm//@types",
        "@npm//rxjs",
    ]
)

ng_module(
    name = "src",
    srcs = glob(
        include = ["**/*.ts"],
        exclude = [
            "**/*.spec.ts",
            "main.ts",
            "test.ts",
            "initialize_testbed.ts",
        ],
    ),
    assets = glob([
      "**/*.css",
      "**/*.html",
    ]) + ([":styles"] if len(glob(["**/*.scss"])) else []),
    deps = [
        "@npm//@angular/core",
        "@npm//@angular/platform-browser",
        "@npm//@angular/router",
        "@npm//@types",
        "@npm//rxjs",
    ],
)