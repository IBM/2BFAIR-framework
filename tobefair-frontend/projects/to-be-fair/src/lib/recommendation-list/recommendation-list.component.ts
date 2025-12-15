import { Component, Input } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'lib-recommendation-list',
  standalone: true,
  imports: [RouterLink, RouterLinkActive],
  templateUrl: './recommendation-list.component.html',
  styleUrl: './recommendation-list.component.css',
})
export class RecommendationListComponent {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  @Input() recommendations!: Array<any>;
  @Input() length: number = 5;
  @Input() redirect_ref?: string;
  should_display_redirect: boolean = true;
  @Input() useSeeMore = true;

  ngOnInit(): void {
    this.should_display_redirect = this.recommendations.length > this.length;
    this.recommendations = this.recommendations.slice(0, this.length);
  }

  ngAfterViewInit(): void {
    if (this.useSeeMore == false) {
      const link = document.getElementById('seeMore');
      if (link) {
        link.style.display = 'none';
      }
    }
  }
}
