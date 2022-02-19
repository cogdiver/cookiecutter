import pathlib

import click

@click.command("create_env", short_help="Create ENV file")
{% if cookiecutter.aws.lower()=='y' -%}
@click.option("-r", "--aws-region", prompt=True, required=True)
@click.option("-k", "--aws-key", prompt=True, required=True)
@click.option("-s", "--aws-secret-key", prompt=True, required=True)
{% endif -%}{% if cookiecutter.s3.lower()=='y' -%}
@click.option("-b", "--bucket", prompt=True, required=True)
{% endif -%}{% if cookiecutter.data_base.lower()=='y' -%}
@click.option("-h", "--database-host", prompt=True, required=False)
@click.option("--database-port", prompt=True, required=False)
@click.option("-u", "--database-user", prompt=True, required=False)
@click.password_option("--database-password", prompt=True, required=False)
@click.option("-n", "--database-name", prompt=True, required=False)
{% endif -%}
def cli(
    {% if cookiecutter.aws.lower()=='y' -%}
    aws_region,
    aws_key,
    aws_secret_key,
    {% endif -%}{% if cookiecutter.s3.lower()=='y' -%}
    bucket,
    {% endif -%}{% if cookiecutter.data_base.lower()=='y' -%}
    database_host,
    database_port,
    database_user,
    database_password,
    database_name
    {% endif -%}
):
    env = pathlib.Path("./.env")
    with env.open("w") as f:
        lines = (
            {% if cookiecutter.aws.lower()=='y' -%}
            f"AWS_REGION={aws_region}",
            f"AWS_KEY={aws_key}",
            f"AWS_SECRET_KEY={aws_secret_key}",
            {% endif -%}{% if cookiecutter.s3.lower()=='y' -%}
            f"BUCKET={bucket}",
            {% endif -%}{% if cookiecutter.data_base.lower()=='y' -%}
            f"DATABASE_HOST={database_host}",
            f"DATABASE_PORT={database_port}",
            f"DATABASE_USER={database_user}",
            f"DATABASE_PASSWORD={database_password}",
            f"DATABASE_NAME={database_name}"
            {% endif -%}
        )
        lines = tuple(map(lambda x: f"{x}\n", lines))
        f.writelines(lines)

    click.echo("✅ ENV file was successfully created ✅")
