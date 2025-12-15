import { Injectable } from "@angular/core";
import { FAIRNotification } from "../models/FAIRnotification";
import { FairnessEvaluation } from "../models/fairness-evaluation";
import { BehaviorSubject } from "rxjs";

@Injectable({
  providedIn: 'root',
})
export class NotificationService {

  private notificationsSubject: BehaviorSubject<FAIRNotification[]> =
      new BehaviorSubject<FAIRNotification[]>([]);

  setNotifications(
      notifications: FAIRNotification[],
    ): void {
      let adaptedNotifications: FAIRNotification[] = [];

      for(let index = 0; index < notifications.length; index++){
        adaptedNotifications.push({
          // Giving an ID to the notification to make it easier to close the notification
          // the ID corresponds to the location of the notification in the notificationSubject array.
          id: index,
          type: notifications[index].type,
          title: notifications[index].title,
          description: notifications[index].description,
          isOpen: true
        });
      };

      this.notificationsSubject.next(adaptedNotifications);
    };

  getNotifications(){
    return this.notificationsSubject
  };

  closeNotification(notificationID:number): void{
    this.notificationsSubject.value[notificationID].isOpen = false;
  };
};
