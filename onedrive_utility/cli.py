import os
import click
import pickle
from .client import Client


class Context(object):
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.session_cache = os.path.expanduser('~/.li_onedrive_session')
        self.config = os.path.expanduser('~/.li_onedrive')
        self.client_id = None
        self.client_secret = None

        if self.config and os.path.isfile(self.config):
            self.load()

    def save(self):
        pickle.dump(self, open(self.config, "wb"))

    def load(self):
        data = pickle.load(open(self.config, "rb"))
        self.__dict__.update(data.__dict__)


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@pass_context
def cli(ctx):
    pass


@cli.command()
@click.option('--client-secret', required=True, help='Application secret')
@click.option('--client-id', required=True, help='Application id')
@pass_context
def init(ctx, client_id, client_secret):
    ctx.client_id = client_id
    ctx.client_secret = client_secret
    ctx.save()

    client = Client(client_id)
    client.authenticate(cache=ctx.session_cache, client_secret=ctx.client_secret)


@cli.command()
@pass_context
def authenticate(ctx):
    client = Client(ctx.client_id)
    client.authenticate(cache=ctx.session_cache, client_secret=ctx.client_secret)


@cli.command()
@click.option('--out', required=False, default="download.out", help='Output file name')
@click.option('-p', required=False, default=False, is_flag=True, help='Print data to output stream')
@click.argument('path', required=True)
@pass_context
def download(ctx, path, out, p):
    client = Client(ctx.client_id)
    client.load_session(ctx.session_cache)
    onedrive_client = client.get_onedrive_client()
    onedrive_client.item(drive='me', path=path).download(out)

    if p:
        with open(out) as file:
            click.echo(file.read())
    else:
        click.echo('output file: {}'.format(out))


def main():
    cli()


if __name__ == "__main__":
    cli()
