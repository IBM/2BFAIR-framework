import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'lib-glossary',
  standalone: true,
  imports: [],
  templateUrl: './glossary.component.html',
  styleUrls: ['./glossary.component.css'],
})
export class GlossaryComponent {
  constructor(private route: ActivatedRoute) {}
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
  }
}
