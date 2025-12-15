/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable no-unused-vars */
import { Component, ElementRef, Input, ViewChild, inject } from '@angular/core';

import { HeaderComponent as LibHeaderComponent } from '../header/header.component';
import { RecommendationListComponent } from '../recommendation-list/recommendation-list.component';
import { Router } from '@angular/router';
import { EvaluationService } from '../evaluation.service';
import { FairnessEvaluation } from '../../models/fairness-evaluation';
import * as d3 from 'd3';
import { LegendComponent } from '../legend/legend.component';
import { getArrayFromDict } from '../functions/functions';
import {
  ESSENTIAL,
  IMPORTANT,
  USEFUL,
  FINDABILITY_CODE,
  ACCESSIBILITY_CODE,
  INTEROPERABILITY_CODE,
  REUSABILITY_CODE,
} from '../constants/constants';

@Component({
  selector: 'lib-explorer',
  standalone: true,
  imports: [LibHeaderComponent, RecommendationListComponent, LegendComponent],
  templateUrl: './explorer.component.html',
  styleUrl: './explorer.component.css',
})
export class ExplorerComponent {
  public detailedResult!: any;

  findability!: number;
  accessibility!: number;
  interoperability!: number;
  reusability!: number;

  @Input() useHeader = true;
  @Input() useSeeMore = true;
  @Input() useArrows = true;

  @ViewChild('divGraph', { static: true })
  divGraph!: ElementRef;

  public evaluationService: EvaluationService = inject(EvaluationService);

  public fairnessEvaluation!: FairnessEvaluation;
  error: any;

  constructor(private router: Router) {}

  private getFAIRnessEvaluation() {
    this.evaluationService
      .getCurrentEvaluation()
      .subscribe((fairnessEvaluationReceived) => {
        this.updateProperties(fairnessEvaluationReceived);
        this.drawGraphic(fairnessEvaluationReceived);
      });
  }

  updateProperties(fairnessEvaluationReceived: FairnessEvaluation): void {
    this.fairnessEvaluation = fairnessEvaluationReceived;
    const detailedResults = this.fairnessEvaluation.detailedResults;
    this.detailedResult = { ...detailedResults };
  }

  public tests: any = [];
  public metrics: number = 0;

  getMetricQuantity(dimension: string) {
    this.tests = [];
    this.metrics = 0;
    let principles =
      this.detailedResult['dimension_results'][dimension]['results'];
    for (let principle of getArrayFromDict(principles)) {
      let keys = Object.keys(principle.results);
      this.metrics += keys.length;
      for (let metric of getArrayFromDict(principle.results)) {
        let priority = 0;

        if (metric.metric_priority === ESSENTIAL) {
          priority = 1;
        } else if (metric.metric_priority === IMPORTANT) {
          priority = 2;
        } else if (metric.metric_priority === USEFUL) {
          priority = 3;
        }

        this.tests.push({
          priority: priority,
          score: metric.metric_score,
          name: metric.metric_id,
        });
      }
    }
    return {
      [`metrics${dimension}`]: this.metrics,
      [`tests${dimension}`]: this.tests,
    };
  }

  private svg: any;

  // Declare the chart dimensions and margins
  private width = 1112;
  private height = 464;
  private marginTop = 20;
  private marginBottom = 10;
  private marginLeft = 260;
  private marginRight = 50;

  private drawGraphic(fairnessEvaluationReceived: FairnessEvaluation) {
    d3.select('#graph').selectAll('svg').remove();

    //Get the current evaluation
    this.fairnessEvaluation = fairnessEvaluationReceived;

    const fairEvaluation = {
      findability: this.fairnessEvaluation.findability,
      accessibility: this.fairnessEvaluation.accessibility,
      interoperability: this.fairnessEvaluation.interoperability,
      reusability: this.fairnessEvaluation.reusability,
    };

    const { metricsF, testsF } = this.getMetricQuantity(FINDABILITY_CODE);
    const { metricsA, testsA } = this.getMetricQuantity(ACCESSIBILITY_CODE);
    const { metricsI, testsI } = this.getMetricQuantity(INTEROPERABILITY_CODE);
    const { metricsR, testsR } = this.getMetricQuantity(REUSABILITY_CODE);

    const colors = {
      blue: ['#ffffff', '#1192E8', '#33b1ff', '#82cfff'],
      red: ['#ffffff', '#FA4D56', '#ff8389', '#ffb3b8'],
      green: ['#ffffff', '#009D9A', '#08bdba', '#3ddbd9'],
      purple: ['#ffffff', '#A56EFF', '#be95ff', '#d4bbff'],
      white: '#ffffff',
    };

    const data = [
      {
        dimension: FINDABILITY_CODE,
        metrics: metricsF,
        color: colors.blue,
        tests: testsF,
        score: fairEvaluation.findability,
      },
      {
        dimension: ACCESSIBILITY_CODE,
        metrics: metricsA,
        color: colors.red,
        tests: testsA,
        score: fairEvaluation.accessibility,
      },
      {
        dimension: INTEROPERABILITY_CODE,
        metrics: metricsI,
        color: colors.green,
        tests: testsI,
        score: fairEvaluation.interoperability,
      },
      {
        dimension: REUSABILITY_CODE,
        metrics: metricsR,
        color: colors.purple,
        tests: testsR,
        score: fairEvaluation.reusability,
      },
    ];

    // Filters dimensions that haven't yet been implemented
    const filteredData = data.filter(function (d) {
      return d.metrics !== 0 && d.tests !== 0;
    });

    // Function to navigate to the Details page
    const navigate = (d: any) => {
      this.router.navigate(['/details'], { fragment: d });
    };

    // Declare the x (horizontal position) scale
    const x = d3
      .scaleLinear() //Defines a quantitative input domain to a continuous output range using a linear transformation
      .domain([0, 100])
      .rangeRound([this.marginRight, this.width - this.marginLeft]);

    // Declare the y (vertical position) scale
    const y = d3
      .scaleBand() // Defines space equally
      .domain(filteredData.map((d) => d.dimension))
      .rangeRound([this.marginBottom, this.height + this.marginTop])
      .padding(2.1);

    const heightSquare = 42;

    this.svg = d3
      .select<SVGElement, any>(this.divGraph.nativeElement)
      .append('svg')
      .attr('width', this.width)
      .attr('height', this.height)
      .attr('viewBox', [0, 0, this.width, this.height])
      .attr('style', 'max-width: 100%; height: auto;');

    this.svg
      .append('g')
      .selectAll('g')
      .data(filteredData)
      .join('g')
      .each(function (this: any, d: any) {
        let currentX = x(0);
        const totalWidth = x(100) - x(0);
        const parent = d3.select(this);
        const width = totalWidth / d.metrics;

        d.tests.forEach((test: any) => {
          const proportionPassed = test.score;
          parent
            .append('rect')
            .attr('y', (y(d.dimension) as number) - 134)
            .attr('x', currentX)
            .attr('height', heightSquare)
            .attr('width', width - 8)
            .attr('fill', colors.white)
            .attr('stroke', d.color[test.priority])
            .attr('stroke-width', '3px');

          if (proportionPassed > 0) {
            parent
              .append('rect')
              .attr('y', (y(d.dimension) as number) - 134)
              .attr('x', currentX)
              .attr('height', heightSquare)
              .attr('width', width * proportionPassed - 8)
              .attr('fill', d.color[test.priority]);
          }

          parent
            .append('text')
            .text(`${test.name}`)
            .attr('x', currentX + width / 2)
            .attr('y', (y(d.dimension) as number) - 134 + heightSquare / 2)
            .attr('dy', '.35em')
            .attr('fill', '#000000')
            .attr('text-anchor', 'middle');

          currentX += width;
        });

        parent
          .append('text')
          .attr('x', x(100) - x(0) + 100)
          .attr('y', (y(d.dimension) as number) - 100)
          .text(`${d.score}%`)
          .classed('total-score', true);

        parent
          .append('a')
          .on('click', function (event) {
            navigate(d.dimension);
          })
          .append('image')
          .attr('xlink:href', '../assets/right-arrow.png')
          .attr('x', x(100) - x(0) + 225)
          .attr('y', (y(d.dimension) as number) - 134)
          .attr('width', heightSquare)
          .attr('height', heightSquare)
          .on('mouseover', function () {
            d3.select(this)
              .transition()
              .duration(500)
              .ease(d3.easeLinear)
              .attr('transform', 'translate(20, 0)');
          })
          .on('mouseout', function () {
            d3.select(this)
              .transition()
              .duration(500)
              .ease(d3.easeLinear)
              .attr('transform', 'translate(0, 0)');
          })
          .classed('hover-image', true);
      });

    this.svg
      .append('g')
      .classed('axis', true)
      .attr('transform', `translate(50, -115)`)
      .call(d3.axisLeft(y).tickSizeOuter(2))
      .call((g: any) => g.select('.domain').remove())
      .call((g: any) => g.selectAll('.tick').selectAll('line').remove());
  }

  ngOnInit(): void {
    this.evaluationService.error$.subscribe((error) => {
      this.error = error;
    });
    this.getFAIRnessEvaluation();
    if (this.useHeader == false) {
      const header = document.getElementById('header');
      if (header) {
        header.style.display = 'none';
      }
    }
  }

  ngAfterViewInit(): void {
    if (this.useArrows == false) {
      const arrows = document.getElementsByClassName('hover-image');
      Array.from(arrows).forEach((arrow) => {
        (arrow as HTMLElement).style.display = 'none';
      });
    }
  }
}
