import { Component, ElementRef, ViewChild, Input } from '@angular/core';
import * as d3 from 'd3';

@Component({
  selector: 'lib-legend',
  standalone: true,
  imports: [],
  templateUrl: './legend.component.html',
  styleUrl: './legend.component.css',
})
export class LegendComponent {
  @ViewChild('legendSvg', { static: true }) legendSvg!: ElementRef;
  @Input() scale: number = 1;

  private baseWidth = 620;
  private baseHeight = 100;
  private marginTop = 20;
  private marginLeft = 70;
  private svg: any;

  constructor(private el: ElementRef) {}

  ngAfterViewInit(): void {
    this.drawLegend();
  }

  private drawLegend(): void {
    if (this.svg) return;

    const legendData = [
      { label: 'Useful', color: '#c6c6c6' },
      { label: 'Important', color: '#a8a8a8' },
      { label: 'Essential', color: '#8d8d8d' },
    ];

    const width = this.baseWidth * this.scale;
    const height = this.baseHeight * this.scale;

    const rectWidth = 85 * this.scale;
    const rectHeight = 42 * this.scale;

    this.svg = d3
      .select(this.legendSvg.nativeElement)
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .attr('viewBox', `0 0 ${this.baseWidth} ${this.baseHeight}`)
      .attr('style', 'max-width: 100%; height: auto;');

    let currentX = this.marginLeft;

    legendData.forEach((d) => {
      this.svg
        .append('rect')
        .attr('x', currentX)
        .attr('y', this.marginTop * this.scale)
        .attr('width', rectWidth)
        .attr('height', rectHeight)
        .style('fill', d.color);

      const textElement = this.svg
        .append('text')
        .attr('x', currentX + rectWidth + 5)
        .attr(
          'y',
          this.marginTop * this.scale + rectHeight / 2 + 5 * this.scale,
        )
        .text(`= ${d.label}`);

      const textWidth = (textElement.node() as SVGTextElement).getBBox().width;

      currentX += rectWidth + textWidth + 20;
    });
  }
}
