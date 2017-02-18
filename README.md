# krlio-python

The "official" python library for [krl.io](krl.io).

## How To Install

`pip install krlio`

#### Installing from Source

```bash
git clone git@github.com/dorthu/krlio-python
cd krlio-python
python3 setup.py install
```

## How to Use

`import krlio`

*krlio.get_link(code)* - returns the URL that shortcode `code` directs to.

*krlio.make_anon_link(url)* - shortens URL and returns the full krl.io shortlink

## Limitations

Currently does not support any authed requests.  All shortlinks are public and
not associated to an account.  Cannot do custom shortlinks at this time.  These
features are coming soon.
