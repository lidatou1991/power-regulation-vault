(function () {
  "use strict";
  var snapshotUrl = new URL("learning-growth.json", document.currentScript.src);
  fetch(snapshotUrl)
    .then(function (response) { if (!response.ok) throw new Error("snapshot unavailable"); return response.json(); })
    .then(function (series) {
      if (!Array.isArray(series.snapshots) || !series.snapshots.length) return;
      var latest = series.snapshots[series.snapshots.length - 1];
      var note = document.getElementById("dataNote");
      if (note) note.textContent = "Day-1 snapshot · " + latest.date + " · future daily snapshots append to this local series";
    })
    .catch(function () { /* Static HTML remains complete without JavaScript. */ });
}());
