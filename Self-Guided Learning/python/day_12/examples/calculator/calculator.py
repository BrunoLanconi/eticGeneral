import click


@click.group()
def cli():
    pass


@cli.group()
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.pass_context
def wildcard(ctx, a, b):
    ctx.obj = {"a": a, "b": b}


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a, b):
    click.echo(a + b)


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def subtract(a, b):
    click.echo(a - b)


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def multiply(a, b):
    click.echo(a * b)


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def divide(a, b):
    click.echo(a / b)


@wildcard.command()
@click.pass_context
def ctx_add(ctx):
    value_a = ctx.obj.get("a")
    value_b = ctx.obj.get("b")

    click.echo(value_a + value_b)


if __name__ == "__main__":
    cli()
