import click


@click.command()
@click.option("--name", default="world", help="Whom to greet.")
def cli(name):
    """
    Say Hello!
    """
    print(f"Hello {name}!")


if __name__ == "__main__":
    cli()
