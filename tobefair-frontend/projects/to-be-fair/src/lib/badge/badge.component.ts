import { Component, ElementRef, inject, Input, ViewChild } from '@angular/core';
import { FairnessEvaluation } from '../../models/fairness-evaluation';
import * as d3 from 'd3';
import { EvaluationService } from '../evaluation.service';

@Component({
  selector: 'lib-badge',
  standalone: true,
  imports: [],
  templateUrl: './badge.component.html',
  styleUrl: './badge.component.css'
})
export class BadgeComponent {
  @Input() fairnessEvaluation: FairnessEvaluation | null = null;
  @Input() useLabel = true;

  @ViewChild('divChart', { static: true })
  divChart!: ElementRef;

  // Inject the service
  evaluationService: EvaluationService = inject(EvaluationService);

  private badge_dimensions = {
    width: 695,
    height: 300,
    marginTop:20,
    marginBottom: 50,
    marginLeft: 20,
    marginRight: 250
  }

  private bar_dimensions = {
    height: this.badge_dimensions.height*0.8,
    gap: 25,
    metric_gap: 10,
    metric_width: 100
  }

  private colors: {[key: string]: any} = {
    'F': {
      'completely_passed': '#1192e8',
      'semi_passed': '#82cfff',
    },
    'A': {
      'completely_passed': '#fa4d56',
      'semi_passed': '#ffb3b8',
    },
    'I': {
      'completely_passed': '#009d9a',
      'semi_passed': '#84dbda',
    },
    'R': {
      'completely_passed': '#a56eff',
      'semi_passed': '#d4bbff',
    },
    'failed': '#ededed',
  }

  getResultsArray(results: any): any[] {
    return Object.values(results);
  }

  getMetricsByDimension(fairnessEvaluation: FairnessEvaluation): {[dimension_id: string]: {'metrics_quantity': number, 'metrics_passed':number, 'metrics_semi_passed':number}}{
    let metrics: {[dimension_id: string]: {'metrics_quantity': number, 'metrics_passed':number, 'metrics_semi_passed':number}} = {};
    for (let result of this.getResultsArray(fairnessEvaluation.detailedResults)) {
      for (let dimension of this.getResultsArray(result)) {
        metrics[dimension.dimension_id] = {'metrics_quantity': 0, 'metrics_passed':0, 'metrics_semi_passed': 0}
        for (let principle of this.getResultsArray(dimension.results)) {
          for (let metric of this.getResultsArray(principle.results)) {
            metrics[dimension.dimension_id]['metrics_quantity'] += 1
            if (metric['metric_score'] > 0){
              if (metric['metric_score'] == 1){
                metrics[dimension.dimension_id]['metrics_passed'] += 1
              }
              else{
                metrics[dimension.dimension_id]['metrics_semi_passed'] += 1
              }

            }
          }
        }
      }
    }
    return metrics
  }

  getMetricHeight(metricQuantity:number, dimensionHeight:number, gap:number){
    if (metricQuantity == 0 || dimensionHeight == 0) {
      return dimensionHeight
    }
    else{
      let metricHeight = (dimensionHeight - (gap * (metricQuantity-1))) / metricQuantity
      return metricHeight
    }
  }

  private svg: any
  private dimensions: any

  private drawBadge(
    fairnessEvaluationReceived: FairnessEvaluation,
    useLabel: boolean,
  ) {

    // Create the SVG container of the badge
    this.svg = d3
    .select<SVGElement, any>(this.divChart.nativeElement)
    .append('svg')
    .attr('width', this.badge_dimensions.width)
    .attr('height', this.badge_dimensions.height)
    .attr('viewBox', [0, 0, this.badge_dimensions.width, this.badge_dimensions.height])
    .attr('style', 'max-width: 100%; height: auto')

    this.svg = this.svg.append('svg')

    // Create dimensions group
    this.dimensions = this.svg
      .append('g')

    // Get dimensions keys
    const dimension_data: {[key: string]: any} = fairnessEvaluationReceived.detailedResults["dimension_results"]
    let dimensions_keys = Object.keys(dimension_data)

    // Get the quantity of metrics in each dimension
    let metrics_data = this.getMetricsByDimension(fairnessEvaluationReceived)

    // Draw metrics box and dimension key
    let x_object_position = 0
    for (let dimension_index in dimensions_keys){
      let dimension_group = this.dimensions.append('g')
      let metrics_group = dimension_group.append('g')

      let dimension_key = dimensions_keys[dimension_index]
      let metric_quantity: number = metrics_data[dimension_key]['metrics_quantity']
      let metric_height = this.getMetricHeight(metric_quantity, this.bar_dimensions.height, this.bar_dimensions.metric_gap)

      let y_object_position = this.bar_dimensions.height - metric_height
      for (let metric_index = 1; metric_index <= metric_quantity; metric_index++){
        // Add metric box
        let metric_group = metrics_group.append("rect")
          .attr("width", this.bar_dimensions.metric_width)
          .attr('height', metric_height)
          .attr('x', x_object_position)
          .attr('y', y_object_position)

        // color metric box
        if (metric_index <= metrics_data[dimension_key]['metrics_passed']){
          metric_group.attr('fill', `${this.colors[dimension_key]['completely_passed']}`)
        }
        else {
          if (metric_index <= metrics_data[dimension_key]['metrics_passed'] + metrics_data[dimension_key]['metrics_semi_passed']) {
            metric_group.attr('fill', `${this.colors[dimension_key]['semi_passed']}`)
          }
          else{
            metric_group.attr('fill', this.colors['failed'])
          }
        }
        y_object_position -= (metric_height + this.bar_dimensions.metric_gap)
      }

      if (useLabel) {
        // add dimension text
        dimension_group.append('text')
        .text(dimension_key)
        .attr('x', x_object_position + this.bar_dimensions.metric_width/2)
        .attr('y', this.bar_dimensions.height + 55)
        .attr("text-anchor", "middle")
        .classed('axis', true);
      }
      x_object_position += this.bar_dimensions.metric_width + this.bar_dimensions.gap
    }

    // add vertical bar
    this.svg.append('rect')
      .attr('width', 5)
      .attr('height', this.bar_dimensions.height)
      .attr('x', x_object_position)
      .classed('bar', true)

    // add the total score value
    let score = this.svg.append('text')
      .attr('x', x_object_position + this.bar_dimensions.gap)
      .attr('y', this.bar_dimensions.height)
      .text(`${Math.round(fairnessEvaluationReceived.totalScore)}`)
      .classed('total-score', true);

      // get score width
      let scoreWidth;
      if (score.node() == null) {
        return undefined;
      } else {
        scoreWidth = score.node().getBBox().width; // Method to determine the coordinates of the smallest rectangle in which the object fits.
        if (scoreWidth == 0) {
          if (fairnessEvaluationReceived.totalScore == 100) {
            scoreWidth = 180;
          } else if (fairnessEvaluationReceived.totalScore >= 10) {
            scoreWidth = 120;
          } else {
            scoreWidth = 60;
          }
        }
      }

    // add the percentage sign
    this.svg.append('text')
      .attr('x', x_object_position + 5 + this.bar_dimensions.gap + scoreWidth)
      .attr('y', this.bar_dimensions.height)
      .text('%')
      .classed('total-score', true)
      .classed('percent-sign', true)
  }

  updateProperties(fairnessEvaluationReceived: FairnessEvaluation): void {
    this.fairnessEvaluation = fairnessEvaluationReceived
  }

  ngOnInit(): void {
    this.evaluationService
      .getCurrentEvaluation()
      .subscribe((fairnessEvaluationReceived) => {
        this.updateProperties(fairnessEvaluationReceived);
        this.drawBadge(fairnessEvaluationReceived, this.useLabel)
      })
  }
}
