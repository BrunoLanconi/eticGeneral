# Lab 37: Add Complexity

Based on the previous lab, you will add more complexity to the calculator application by implementing contexts.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. In `calculator.py`, add a `group` object called `wildcard` to `cli`.

```python
...

@cli.group()
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.pass_context
def wildcard(ctx, a, b):
    ctx.obj = {"a": a, "b": b}
```

This group will take two arguments, `a` and `b`, and store them in a context object.

2. Create a command called `ctx_add` that adds the two numbers stored in the context object.

```python
...

@wildcard.command()
@click.pass_context
def ctx_add(ctx):
    value_a = ctx.obj.get("a")
    value_b = ctx.obj.get("b")

    click.echo(value_a + value_b)
```

### Optional Challenge

- Adapt `cli` to be the new `wildcard` group. This will allow you to use the `cli` group to store the context object.
- Delete the `wildcard` group and the `ctx_add` command and adapt `subtract`, `multiply`, and `divide` to use the context object.