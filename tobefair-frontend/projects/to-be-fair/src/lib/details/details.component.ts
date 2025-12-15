/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { HeaderComponent as LibHeaderComponent } from '../header/header.component';
import { CarbonModule } from '../carbon/carbon.module';
import { Component, inject, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {
  AccordionModule,
  TilesModule,
  IconService,
} from 'carbon-components-angular';
import { FairnessEvaluation } from '../../models/fairness-evaluation';
import {
  CircleStrokeGlyph,
  CheckmarkFilled16,
  CheckmarkFilledError16,
  WarningAlt20,
  Growth20,
  Report20,
} from '@carbon/icons';
import { EvaluationService } from '../evaluation.service';
import { ErrorComponent } from '../error/error.component';

const PASSED_SVG = `
  <svg cdsIcon="checkmark--filled" size="16" fill="#24a148" class="cds--btn__icon" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" style="margin-right: 8px">
    <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
    <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
  </svg>
`;

const FAILED_SVG = `
  <svg cdsIcon="error--filled" size="16" fill="#da1e28" class="cds--btn__icon" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" style="margin-right: 8px">
    <path d="M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M10.7,11.5L4.5,5.3l0.8-0.8l6.2,6.2L10.7,11.5z"></path>
    <path fill="none" d="M10.7,11.5L4.5,5.3l0.8-0.8l6.2,6.2L10.7,11.5z" data-icon-path="inner-path" opacity="0"></path>
  </svg>
`;

const NOT_EXECUTED_SVG = `
  <svg cdsIcon="circle-stroke" size="glyph" fill="#6f6f6f" class="cds--btn__icon" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" style="margin-right: 8px">
    <path d="M8,4A4,4,0,1,1,4,8,4.0045,4.0045,0,0,1,8,4M8,2a6,6,0,1,0,6,6A6,6,0,0,0,8,2Z"></path>
  </svg>
`;

@Component({
  selector: 'lib-details',
  standalone: true,
  imports: [
    LibHeaderComponent,
    AccordionModule,
    CarbonModule,
    TilesModule,
    ErrorComponent,
  ],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
})
export class DetailsComponent implements OnInit {
  @Input() useHeader = true;
  @Input() expanded = false;
  public detailedResult!: any;

  public evaluationService: EvaluationService = inject(EvaluationService);

  public fairnessEvaluation!: FairnessEvaluation;
  size!: 'sm' | 'md' | 'lg';
  error: any;

  // eslint-disable-next-line no-unused-vars
  constructor(
    private route: ActivatedRoute,
    iconService: IconService,
  ) {
    iconService.registerAll([
      CircleStrokeGlyph,
      CheckmarkFilled16,
      CheckmarkFilledError16,
      WarningAlt20,
      Growth20,
      Report20,
    ]);
  }

  updateProperties(fairnessEvaluationReceived: FairnessEvaluation): void {
    this.fairnessEvaluation = fairnessEvaluationReceived;
    const detailedResults = this.fairnessEvaluation.detailedResults;
    this.detailedResult = { ...detailedResults };
  }

  getArrayFromDict(results: any): any[] {
    return Object.values(results);
  }

  selected(event: any, test: any) {
    const id = test.test_id;
    const accordionItems = document.querySelectorAll('cds-accordion-item');

    accordionItems.forEach((accordionItem) => {
      const button = accordionItem.querySelector('button');
      const attribute = button?.getAttribute('aria-controls');
      if (attribute !== id) return;

      if (!event.expanded) {
        this.updateTitle(test);
      } else {
        button?.querySelector('span')?.remove();
      }
    });
  }

  getTitle(test: any): string {
    return `
      ${test.test_id} : ${test.test_name}
    `;
  }

  updateTitle(test: any) {
    const id = test.test_id;
    const accordionItems = document.querySelectorAll('cds-accordion-item');

    accordionItems.forEach((accordionItem) => {
      const button = accordionItem.querySelector('button');
      const attribute = button?.getAttribute('aria-controls');
      if (attribute !== id) return;

      let p = button?.querySelector('p');
      const span = document.createElement('span');
      span.style.fontSize = '12px';
      span.style.color = '#6f6f6f';
      span.style.display = 'inline-flex';
      span.style.alignItems = 'center';
      span.style.marginLeft = '8px';

      if (test.status === 'passed') {
        span.innerHTML = `${PASSED_SVG} Passed • ${test.score}/${test.max_score} `;
      } else if (test.status === 'failed') {
        span.innerHTML = `${FAILED_SVG} Failed • ${test.score}/${test.max_score}`;
      } else {
        span.innerHTML = `${NOT_EXECUTED_SVG} Not Executed • ${test.score}/${test.max_score}`;
      }

      p?.appendChild(span);
      p!.style.display = 'inline-flex';
    });
  }

  ngOnInit(): void {
    this.evaluationService.error$.subscribe((error) => {
      this.error = error;
    });
    this.evaluationService
      .getCurrentEvaluation()
      .subscribe((fairnessEvaluationReceived) => {
        this.updateProperties(fairnessEvaluationReceived);
      });
    if (this.useHeader == false) {
      const header = document.getElementById('details-header');
      if (header) {
        header.style.display = 'none';
      }
    }
  }

  ngAfterViewInit(): void {
    this.route.fragment.subscribe((fragment: string | null) => {
      if (fragment) {
        setTimeout(() => {
          document
            .getElementById(fragment)
            ?.scrollIntoView({ behavior: 'smooth' });
        }, 0);
      }
    });
    if (!this.expanded){
      for (let result of this.getArrayFromDict(this.detailedResult)) {
        for (let dimension of this.getArrayFromDict(result)) {
          for (let principle of this.getArrayFromDict(dimension.results)) {
            for (let metric of this.getArrayFromDict(principle.results)) {
              this.getArrayFromDict(metric.results).forEach((test) => {
                this.updateTitle(test);
              });
            }
          }
        }
      }
    }
  }
}
