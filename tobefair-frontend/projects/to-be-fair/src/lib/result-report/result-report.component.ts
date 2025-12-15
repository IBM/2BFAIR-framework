import { Component, ElementRef, ViewChild } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { ResultComponent } from '../result/result.component';
import { ExplorerComponent } from '../explorer/explorer.component';
import { DetailsComponent } from '../details/details.component';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';
import { Download20 } from '@carbon/icons';
import { ButtonModule, IconService } from 'carbon-components-angular';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'lib-result-report',
  standalone: true,
  imports: [
    HeaderComponent,
    ResultComponent,
    ExplorerComponent,
    DetailsComponent,
    ButtonModule,
  ],
  templateUrl: './result-report.component.html',
  styleUrl: './result-report.component.css',
})
export class ResultReportComponent {
  public expanded: BehaviorSubject<boolean> =
      new BehaviorSubject<boolean>(false);

  constructor(iconService: IconService) {
    iconService.registerAll([Download20]);
  }

  public generatePDF() {
    this.expanded.next(true)
    const element = document.getElementById('content');

    if (!element) {
      console.error('The element was not found!');
      return;
    }

    html2canvas(element, { scale: 2 }).then((canvas: any) => {
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'mm', 'a4');

      const imgWidth = 210;
      const pageHeight = 297;
      const imgHeight = (canvas.height * imgWidth) / canvas.width;

      let position = 0;

      while (position < imgHeight) {
        pdf.addImage(imgData, 'PNG', 0, -position, imgWidth, imgHeight);
        position += pageHeight;

        if (position < imgHeight) {
          pdf.addPage();
        }
      }

      pdf.save('result-report.pdf');
    });

    // html2canvas(element, { scale: 0.5 }).then((canvas: any) => {
    //   const imgWidth = 210;
    //   const pageHeight = 297;
    //   const imgHeight = (canvas.height * imgWidth) / canvas.width;

    //   const pdf = new jsPDF('p', 'mm', 'a4');
    //   const pageCanvasHeight = (canvas.width * pageHeight) / imgWidth;

    //   let position = 0;
    //   let pageCount = 0;

    //   while (position < canvas.height) {
    //     const pageCanvas = document.createElement('canvas');
    //     pageCanvas.width = canvas.width;
    //     pageCanvas.height = Math.min(
    //       pageCanvasHeight,
    //       canvas.height - position,
    //     );

    //     const ctx = pageCanvas.getContext('2d');
    //     if (ctx) {
    //       ctx.drawImage(
    //         canvas,
    //         0,
    //         position,
    //         canvas.width,
    //         pageCanvas.height,
    //         0,
    //         0,
    //         canvas.width,
    //         pageCanvas.height,
    //       );
    //     }

    //     const imgData = pageCanvas.toDataURL('image/png');
    //     if (pageCount > 0) pdf.addPage();
    //     pdf.addImage(
    //       imgData,
    //       'PNG',
    //       0,
    //       0,
    //       imgWidth,
    //       (pageCanvas.height * imgWidth) / canvas.width,
    //     );

    //     position += pageCanvasHeight;
    //     pageCount++;
    //   }

    //   pdf.save('result-report.pdf');
    // });
  }
}
