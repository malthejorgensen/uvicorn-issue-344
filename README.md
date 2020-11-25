# Uvicorn issue 344

This is a repository demonstrating [uvicorn issue 344](https://github.com/encode/uvicorn/issues/344).

You can find this code deployed at <https://uvicorn-issue-344.herokuapp.com>.

In order to reproduce the bug simply submit the form that is shown in the app 3-5 times.
What happens is that Uvicorn breaks the connection and Heroku throws an error.

You can also deploy this project to Heroku yourself by using the button below.

<table>
  <thead>
    <tr>
      <th>Description</th>
      <th>Branch name</th>
      <th>Has issue?</th>
      <th>Deploy to Heroku</th>
      <th>Pre-deployed URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>uvicorn v0.11.8</td>
      <td><code>quart</code></td>
      <td>No</td>
      <td><a href="https://heroku.com/deploy?template=https://github.com/malthejorgensen/uvicorn-issue-344/tree/quart"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy uvicorn v0.11.8"></a></td>
      <td><a href="https://uvicorn-issue-344.herokuapp.com/">https://uvicorn-issue-344.herokuapp.com/</a></td>
    </tr>
    <tr>
      <td>uvicorn v0.11.8 /w patch</td>
      <td><code>quart-patched-uvicorn</code></td>
      <td>Yes</td>
      <td><a href="https://heroku.com/deploy?template=https://github.com/malthejorgensen/uvicorn-issue-344/tree/quart-patched-uvicorn"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy uvicorn v0.11.8 /w patch"></a></td>
      <td><a href="https://uvicorn-issue-344-patched.herokuapp.com/">https://uvicorn-issue-344-patched.herokuapp.com/</a></td>
    </tr>
    <tr>
      <td>uvicorn v0.12.3 (latest)</td>
      <td><code>quart-uvicorn-v0.12.3</code></td>
      <td>No</td>
      <td><a href="https://heroku.com/deploy?template=https://github.com/malthejorgensen/uvicorn-issue-344/tree/quart-uvicorn-v0.12.3"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy uvicorn v0.12.3"></a></td>
      <td><a href="https://uvicorn-issue-344-v0-12-3.herokuapp.com/">https://uvicorn-issue-344-v0-12-3.herokuapp.com/</a></td>
    </tr>
  </tbody>
</table>
_Note: uvicorn v0.12.3 is the latest version as of the time of writing (2020-11-26)._
