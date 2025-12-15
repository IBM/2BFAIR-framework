import { inject, Injectable } from '@angular/core';
import { FairnessEvaluationAPI } from '../models/fairness-evaluation-api';
import { FairnessEvaluation } from '../models/fairness-evaluation';
import { BehaviorSubject, catchError, Observable, throwError } from 'rxjs';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { EnvVarGuard } from './env-var.guard';
import { NotificationService } from './notification.service';

const storageKey = 'storage';
@Injectable({
  providedIn: 'root',
})
export class EvaluationService {
  mockFairnessEvaluation: FairnessEvaluation = {
    evaluationId:
      'Placeholder ID (ideally, the evaluation ID should be FAIR too!)',

    evaluatedDigitalObjectID: 'https://example.com/placeholderData',
    evaluatedMetadataRecordID: 'https://example.com/placeholderMetadata',
    community: 'Placeholder community',
    task: 'Placeholder task',

    findability: 0,
    accessibility: 0,
    interoperability: 0,
    reusability: 0,
    totalScore: 0,
    priorityRecommendations: [{
      "recommendation": "Recommendation description.",
      "test_id": "Test ID",
      "dimension_id": "Dimension ID"
    }],
    detailedResults: {
      "dimension_results": {
        "F": {
          "dimension_id": "F",
          "dimension_name": "Dimension name",
          "results": {
            "Principle": {
              "principle_id": "Principle ID",
              "principle_name": "Principle name.",
              "results": {
                "Metric": {
                  "alternate_test_behavior": "skip",
                  "metric_id": "Metric ID",
                  "metric_name": "Metric name.",
                  "metric_priority": "Essential",
                  "metric_maturity": "Advanced",
                  "scoring_mechanism": "Alternative",
                  "results": {
                    "Test": {
                      "test_id": "Test ID",
                      "test_name": "Test name.",
                      "score": 0,
                      "max_score": 0.0,
                      "maturity": {
                        "value": "Incomplete"
                      },
                      "result_description": "Test description.",
                      "result_details": null,
                      "evaluated_requirements": null,
                      "status": "failed",
                      "recommendation": "Test recommendation.",
                      "recommendation_details": "Test recommendation details.",
                      "losses": "Test losses."
                    },
                  },
                  "metric_score": 0
                },
              },
              "score": 0
            },
          }
        },
        "A": {
          "dimension_id": "A",
          "dimension_name": "Dimension name",
          "results": {
            "Principle": {
              "principle_id": "Principle ID",
              "principle_name": "Principle name.",
              "results": {
                "Metric": {
                  "alternate_test_behavior": "skip",
                  "metric_id": "Metric ID",
                  "metric_name": "Metric name.",
                  "metric_priority": "Essential",
                  "metric_maturity": "Advanced",
                  "scoring_mechanism": "Alternative",
                  "results": {
                    "Test": {
                      "test_id": "Test ID",
                      "test_name": "Test name.",
                      "score": 0,
                      "max_score": 0.0,
                      "maturity": {
                        "value": "Incomplete"
                      },
                      "result_description": "Test description.",
                      "result_details": null,
                      "evaluated_requirements": null,
                      "status": "failed",
                      "recommendation": "Test recommendation.",
                      "recommendation_details": "Test recommendation details.",
                      "losses": "Test losses."
                    },
                  },
                  "metric_score": 0
                },
              },
              "score": 0
            },
          }
        },
        "I": {
          "dimension_id": "I",
          "dimension_name": "Dimension name",
          "results": {
            "Principle": {
              "principle_id": "Principle ID",
              "principle_name": "Principle name.",
              "results": {
                "Metric": {
                  "alternate_test_behavior": "skip",
                  "metric_id": "Metric ID",
                  "metric_name": "Metric name.",
                  "metric_priority": "Essential",
                  "metric_maturity": "Advanced",
                  "scoring_mechanism": "Alternative",
                  "results": {
                    "Test": {
                      "test_id": "Test ID",
                      "test_name": "Test name.",
                      "score": 0,
                      "max_score": 0.0,
                      "maturity": {
                        "value": "Incomplete"
                      },
                      "result_description": "Test description.",
                      "result_details": null,
                      "evaluated_requirements": null,
                      "status": "failed",
                      "recommendation": "Test recommendation.",
                      "recommendation_details": "Test recommendation details.",
                      "losses": "Test losses."
                    },
                  },
                  "metric_score": 0
                },
              },
              "score": 0
            },
          }
        },
        "R": {
          "dimension_id": "R",
          "dimension_name": "Dimension name",
          "results": {
            "Principle": {
              "principle_id": "Principle ID",
              "principle_name": "Principle name.",
              "results": {
                "Metric": {
                  "alternate_test_behavior": "skip",
                  "metric_id": "Metric ID",
                  "metric_name": "Metric name.",
                  "metric_priority": "Essential",
                  "metric_maturity": "Advanced",
                  "scoring_mechanism": "Alternative",
                  "results": {
                    "Test": {
                      "test_id": "Test ID",
                      "test_name": "Test name.",
                      "score": 0,
                      "max_score": 0.0,
                      "maturity": {
                        "value": "Incomplete"
                      },
                      "result_description": "Test description.",
                      "result_details": null,
                      "evaluated_requirements": null,
                      "status": "failed",
                      "recommendation": "Test recommendation.",
                      "recommendation_details": "Test recommendation details.",
                      "losses": "Test losses."
                    },
                  },
                  "metric_score": 0
                },
              },
              "score": 0
            },
          }
        },
      }
    },
    evaluatedDigitalObjectLandingPageUrl: '',
    evaluatedMetadata: {},
    notifications: [{id: 1, type: 'error', title: 'Test Notification', description: 'Test description.', isOpen: true}],
  };

  private isLoadingSubject: BehaviorSubject<boolean> =
    new BehaviorSubject<boolean>(false);
  public isLoading$ = this.isLoadingSubject.asObservable();

  public errorSubject: BehaviorSubject<string | null> = new BehaviorSubject<
    string | null
  >(null);
  public error$ = this.errorSubject.asObservable();

  public dataSubject: BehaviorSubject<FairnessEvaluation>;

  public notificationService: NotificationService = inject(NotificationService);

  constructor(
    private http: HttpClient,
    private _envVarGuard: EnvVarGuard,
  ) {
    const storedData = this.getData(storageKey);
    if (storedData) {
      this.mockFairnessEvaluation = storedData;
    };
    this.dataSubject = new BehaviorSubject<FairnessEvaluation>(
      this.mockFairnessEvaluation,
    );
  };

  getData(key: string): any {
    const item = localStorage.getItem(key);
    if (item === null) {
      return null;
    };
    return JSON.parse(item);
  };

  setData(key: string, data: any) {
    localStorage.setItem(key, JSON.stringify(data));
  };

  requestStandalone(digitalObjectURI: string, community: string, task: string) {
    localStorage.clear();
    let backendPath = `${this._envVarGuard.backendUrl}/evaluate`;

    let requestBody = JSON.stringify({
      resource_id: digitalObjectURI,
      community: community,
      task: task,
    });
    console.log('This is the request body JSON:', requestBody);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
    };

    this.isLoadingSubject.next(true);
    this.errorSubject.next(null);

    this.http
      .post<FairnessEvaluationAPI>(backendPath, requestBody, httpOptions)
      .pipe(catchError((error) => this.handleError(error)))
      .subscribe((fairnessEvaluationReceived) => {
        localStorage.clear();
        console.log(
          'This is the response from requestEvaluation:',
          fairnessEvaluationReceived,
        );

        this.dataSubject.next(this.adaptEvaluation(fairnessEvaluationReceived));
        this.notificationService.setNotifications(this.dataSubject.value.notifications)
      });
  };

  // This method adapts the data received as the response, to reduce coupling
  adaptEvaluation(
    fairnessEvaluationReceived: FairnessEvaluationAPI,
  ): FairnessEvaluation {
    let state;
    let adaptedFairnessEvaluation: FairnessEvaluation = {
      evaluationId: fairnessEvaluationReceived.overall_result.evaluation_id,
      evaluatedDigitalObjectID:
        fairnessEvaluationReceived.overall_result.evaluated_digital_object_id,
      evaluatedMetadataRecordID:
        fairnessEvaluationReceived.overall_result.evaluated_metadata_record_id,
      community: fairnessEvaluationReceived.overall_result.community,
      task: fairnessEvaluationReceived.overall_result.task,
      findability:
        fairnessEvaluationReceived.overall_result.evaluation_score.Findability,
      accessibility:
        fairnessEvaluationReceived.overall_result.evaluation_score
          .Accessibility,
      interoperability:
        fairnessEvaluationReceived.overall_result.evaluation_score
          .Interoperability,
      reusability:
        fairnessEvaluationReceived.overall_result.evaluation_score.Reusability,
      totalScore:
        fairnessEvaluationReceived.overall_result.evaluation_score.total_score,
      priorityRecommendations:
        fairnessEvaluationReceived.overall_result.priority_recommendations,
      detailedResults: fairnessEvaluationReceived.detailed_results,
      evaluatedDigitalObjectLandingPageUrl:
        fairnessEvaluationReceived.overall_result
          .evaluated_digital_object_landing_page_url,
      evaluatedMetadata: fairnessEvaluationReceived.evaluated_metadata,
      notifications: fairnessEvaluationReceived.notifications,
    };

    this.dataSubject.next(adaptedFairnessEvaluation);
    this.setData(storageKey, adaptedFairnessEvaluation);
    this.logCurrentEvaluation();

    return adaptedFairnessEvaluation;
  };

  logCurrentEvaluation(): void {
    console.log('Current evaluation:', this.dataSubject.getValue());
    this.isLoadingSubject.next(false);
  };

  getCurrentEvaluation(): Observable<FairnessEvaluation> {
    return this.dataSubject.asObservable();
  };

  handleError(error: HttpErrorResponse) {
    let errorMessage = 'An unexpected error occurred';
    if (error.status === 404) {
      errorMessage = error.error?.detail || 'Resource not found';
    } else {
      errorMessage = error.message;
    };
    console.error('Error:', errorMessage);
    this.errorSubject.next(errorMessage);
    this.isLoadingSubject.next(false);
    return throwError(() => new Error(errorMessage));
  };
};
