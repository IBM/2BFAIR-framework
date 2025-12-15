import { Component, inject, OnInit, Input } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

import { FairnessEvaluation } from '../../models/fairness-evaluation';

import { BadgeComponent as LibBadgeComponent } from '../badge/badge.component';
import { EvaluationService } from '../evaluation.service';
import { NotificationService } from '../notification.service';
import { FAIRNotification } from "../../models/FAIRnotification";
import { ButtonModule, LoadingModule, NotificationModule} from 'carbon-components-angular';

import { ErrorComponent } from '../error/error.component';

@Component({
  selector: 'lib-result',
  standalone: true,
  imports: [
    LibBadgeComponent,
    RouterLink,
    RouterLinkActive,
    ButtonModule,
    LoadingModule,
    NotificationModule,
    ErrorComponent,
  ],
  templateUrl: './result.component.html',
  styleUrl: './result.component.css',
})
export class ResultComponent implements OnInit {
  public fairnessEvaluation!: FairnessEvaluation;
  public notifications!: Array<FAIRNotification>;

  public isLoading: boolean = false;
  @Input() digitalObjectID: string = '(placeholder digital object ID)';
  public metadataRecordID: string = '(placeholder metadata record ID)';
  @Input() community: string = '(placeholder community)';
  @Input() task: string = '(placeholder task)';
  @Input() useButton = true;

  public doidHref: string | undefined;
  public mridHref: string | undefined;
  public error: any | undefined;

  public evaluationService: EvaluationService = inject(EvaluationService);
  public notificationService: NotificationService = inject(NotificationService);
  router: any;
  constructor() {};

  getFAIRnessEvaluation() {
    this.evaluationService
      .getCurrentEvaluation()
      .subscribe((fairnessEvaluationReceived) => {
        this.updateProperties(fairnessEvaluationReceived);
      });
  };

  getNotifications() {
    this.notificationService
    .getNotifications()
    .subscribe((notificationsReceived) => {
      this.notifications = notificationsReceived
    });
  };

  closeNotification(notificationID:number){
    this.notificationService.closeNotification(notificationID);
  };

  ngOnInit(): void {
    this.evaluationService.error$.subscribe((error) => {
      this.error = error;
    });
    this.evaluationService.isLoading$.subscribe((isLoading) => {
      this.isLoading = isLoading;
    });

    this.getFAIRnessEvaluation();
    this.getNotifications();
  };

  ngAfterViewInit(): void {
    if (this.useButton == false) {
      const button = document.getElementById('explorer-button');
      if (button) {
        button.style.display = 'none';
      };
    };
  };

  checkURI(results: any) {
    this.doidHref = undefined;
    this.mridHref = undefined;
    const test =
      results['dimension_results']['F']['results']['F1']['results']['F1-02D'][
        'results'
      ]['F1-02D-1'];
    if (test.status === 'passed') {
      this.doidHref = this.digitalObjectID;
      this.mridHref = this.metadataRecordID;
    };
  };

  updateProperties(fairnessEvaluationReceived: FairnessEvaluation): void {
    this.fairnessEvaluation = fairnessEvaluationReceived;
    this.digitalObjectID = this.fairnessEvaluation.evaluatedDigitalObjectID;
    this.metadataRecordID = this.fairnessEvaluation.evaluatedMetadataRecordID;
    this.community = this.fairnessEvaluation.community;
    this.task = this.fairnessEvaluation.task;
    const href = this.fairnessEvaluation.detailedResults;
    this.checkURI(href);
  };
};
