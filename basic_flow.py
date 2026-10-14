from prefect import flow, get_run_logger, task


@task(retries=2, retry_delay_seconds=5)
def extract() -> list[int]:
    get_run_logger().info("Extracting data")
    return [1, 2, 3, 4, 5]


@task
def transform(values: list[int]) -> list[int]:
    return [value * 10 for value in values]


@task
def load(values: list[int]) -> None:
    get_run_logger().info("Loaded values: %s", values)


@flow(name="basic-etl")
def basic_etl() -> None:
    values = extract()
    transformed = transform(values)
    load(transformed)
