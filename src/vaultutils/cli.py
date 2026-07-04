import click
from .config import load_config
from .rotate import Rotator


@click.group()
def main():
    """vaultutils command line."""


@main.command()
@click.argument("name")
@click.option("--env", default=".env")
def rotate(name, env):
    cfg = load_config(env)
    click.echo(Rotator(cfg).rotate(name))


if __name__ == "__main__":
    main()
