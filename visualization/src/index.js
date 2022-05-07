import "./styles.css";

import * as d3 from "d3";
import { sankey as d3sankey, sankeyLinkHorizontal } from "d3-sankey";
import DOM from "@observablehq/stdlib/src/dom/index.js";

import data from "./data";

const width = 600;
const height = 500;

const ENABLE_LINKS_GRADIENTS = true;

const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

const { nodes, links } = d3sankey()
  .nodeId((d) => d.name)
  .nodeWidth(5)
  .nodePadding(5)
  .extent([
    [1, 1],
    [width - 1, height - 5],
  ])(data);
console.log({ nodes, links });

//console.log(data);
//console.log(
//  sankey({
//    nodes: data.nodes,
//    links: data.links
//  })
//);

//const { nodes, links } = sankey()(data);
//console.log(nodes, links);

function format(d) {
  const format = d3.format(",.0f");
  return data.units ? (d) => `${format(d)} ${data.units}` : format;
}

svg
  .append("g")
  .attr("stroke", "#000")
  .attr("stroke-width", "0")
  .selectAll("rect")
  .data(nodes)
  .join("rect")
  .attr("x", (d) => d.x0)
  .attr("y", (d) => d.y0)
  .attr("height", (d) => d.y1 - d.y0)
  .attr("width", (d) => d.x1 - d.x0)
  .attr("fill", (d) => d.color)
  .append("title")
  .text((d) => `${d.name}\n${format(d.value)}`);

const link = svg
  .append("g")
  .attr("fill", "none")
  .attr("stroke-opacity", 0.5)
  .selectAll("g")
  .data(links)
  .join("g");
//.style("mix-blend-mode", "multiply");

if (ENABLE_LINKS_GRADIENTS) {
  const gradient = link
    .append("linearGradient")
    .attr("id", (d) => (d.uid = DOM.uid("link")).id)
    .attr("gradientUnits", "userSpaceOnUse")
    .attr("x1", (d) => d.source.x1)
    .attr("x2", (d) => d.target.x0);

  gradient
    .append("stop")
    .attr("offset", "0%")
    .attr("stop-color", (d) => d.source.color);

  gradient
    .append("stop")
    .attr("offset", "100%")
    .attr("stop-color", (d) => d.target.color);
}
link
  .append("path")
  .attr("d", sankeyLinkHorizontal())
  .attr("stroke", (d) => (!ENABLE_LINKS_GRADIENTS ? "#f00" : d.uid))
  .attr("stroke-width", (d) => Math.max(1, d.width));

link
  .append("title")
  .text((d) => `${d.source.name} → ${d.target.name}\n${format(d.value)}`);

svg
  .append("g")
  .attr("font-family", "sans-serif")
  .attr("font-size", 10)
  .selectAll("text")
  .data(nodes)
  .join("text")
  .attr("x", (d) => (d.x0 < width / 2 ? d.x1 + 6 : d.x0 - 6))
  .attr("y", (d) => (d.y1 + d.y0) / 2)
  .attr("dy", "0.35em")
  .attr("text-anchor", (d) => (d.x0 < width / 2 ? "start" : "end"))
  .text((d) => d.name);

const domNode = svg.node();
console.log(domNode);
document.body.appendChild(domNode);
