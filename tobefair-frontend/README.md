# 2BFAIR-Frontend

This is the frontend application for the 2BFAIR project, built with Angular.

- To run the 2BFAIR-frontend, the 2BFAIR-backend should be run. You can start the backend locally or use the backend running on the cluster.
You define the 2BFAIR-backend to be used by setting the environment variable `BACKEND_URL`, e.g., `export BACKEND _URL =http://localhost:8000`.
- Note that if the variable is not set, the backend running locally will be considered. It is defined in `server.js` through:

```js
app.get("/get-backend", (req, res) => {
  res.send(process.env.BACKEND_URL ?? "http://localhost:8000");
});
```

- Check if the `BACKEND_URL` is pointing out to where the backend is running: `echo $BACKEND_URL`.
- Install the dependencies: `npm install --legacy-peer-deps`
- Build the application: `ng build`
- Start the application: `npm run server`
- Access the application at [http://localhost:42000](http://localhost:42000).

## To reflect code changes

- After making changes to the code, run `ng build` to build the project. This command compiles the Angular application into static files in the /`dist` directory.
- For active development, consider using `ng serve` instead of `npm run server`. The former command automatically reflects code changes without the need for a manual build. In this case, you access the application at [http://localhost:4200](http://localhost:4200).
