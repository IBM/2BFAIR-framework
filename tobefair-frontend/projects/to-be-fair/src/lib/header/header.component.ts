import { Component, Input, OnInit, ViewChild, inject } from '@angular/core';
import { Download20 } from '@carbon/icons';
import { IconService } from 'carbon-components-angular';
import { FairnessEvaluation } from '../../models/fairness-evaluation';
import { BadgeComponent as LibBadgeComponent } from '../badge/badge.component';
import { EvaluationService } from '../evaluation.service';
import { CarbonModule } from '../carbon/carbon.module';
@Component({
  selector: 'lib-header',
  standalone: true,
  imports: [LibBadgeComponent, CarbonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
})
export class HeaderComponent implements OnInit {
  @Input() useDownload = true;
  fairnessEvaluation!: FairnessEvaluation;

  digitalObjectID: string = '(placeholder digital object ID)';
  metadataRecordID: string = '(placeholder metadata record ID)';
  community: string = '(placeholder community)';
  task: string = '(placeholder task)';
  digitalObjectLandingPageUrl: string = '(placeholder digital object URL)';

  evaluationService: EvaluationService = inject(EvaluationService);

  constructor(iconService: IconService) {
    iconService.registerAll([Download20]);
  }

  ngOnInit(): void {
    this.evaluationService
      .getCurrentEvaluation()
      .subscribe((fairnessEvaluationReceived) => {
        this.updateProperties(fairnessEvaluationReceived);
      });
    if (this.useDownload == false) {
      const button = document.getElementById('download');
      if (button) {
        button.style.display = 'none';
      }
    }
  }

  updateProperties(fairnessEvaluationReceived: FairnessEvaluation): void {
    this.fairnessEvaluation = fairnessEvaluationReceived;
    this.digitalObjectID = this.fairnessEvaluation.evaluatedDigitalObjectID;
    this.metadataRecordID = this.fairnessEvaluation.evaluatedMetadataRecordID;
    this.community = this.fairnessEvaluation.community;
    this.task = this.fairnessEvaluation.task;
    this.digitalObjectLandingPageUrl =
      this.fairnessEvaluation.evaluatedDigitalObjectLandingPageUrl;
  }

  public saveResponse(): void {
    const response = this.fairnessEvaluation;

    if (!response) {
      return;
    }

    const json = JSON.stringify(response);

    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'evaluation-result.json';
    document.body.appendChild(a);
    a.click();

    setTimeout(() => {
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    }, 0);
  }
}
