from dagster import pipeline, ModeDefinition, fs_io_manager, local_file_manager

from definitions.exchangerates.solids import extract, load, transform, visualize


def load_exchangerates_pipline():
    @pipeline(
        mode_defs=[
            ModeDefinition(
                resource_defs={"io_manager": fs_io_manager, "file_manager": local_file_manager}
            )
        ]
    )
    def exchangerates_pipline():
        visualize(load(transform(extract())))

    return exchangerates_pipline
