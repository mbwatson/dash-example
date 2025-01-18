window.dash_clientside = Object.assign({}, window.dash_clientside, {
  clientside: {
    local_script_callback: function(n_clicks = 0) {
      console.log(`click count: ${n_clicks}`)
      return n_clicks;
    }
  }
});
