import urllib

from quart import Quart, redirect, request

app = Quart(__name__)


@app.route('/view', methods=['GET', 'POST'])
async def view():
    params = request.args
    return f'''<!doctype html>
<html>
  <body>
    <pre>
      {params['story']}
  </pre>
  </body>
</html>
'''


@app.route('/create-new', methods=['POST'])
async def redir():
    params = await request.form
    return redirect(f'view?{urllib.parse.urlencode(params)}')


@app.route('/')
async def index():
    long_str = ''
    for i in range(1000):
        long_str += f'{i} '

    return f'''<!doctype html>
<html>
  <body>
    <form method="POST" action="/create-new">
      <textarea name="story">{long_str}</textarea>
      <button>Submit</button>
    </form>
  </body>
</html>
'''


if __name__ == '__main__':
    app.run()
